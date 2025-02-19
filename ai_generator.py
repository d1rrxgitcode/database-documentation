import re
from ctransformers import AutoModelForCausalLM

def setup_local_ai():
    try:
        model = AutoModelForCausalLM.from_pretrained(
            'TheBloke/TinyLlama-1.1B-Chat-v0.3-GGUF',
            model_file='tinyllama-1.1b-chat-v0.3.q2_K.gguf',
            model_type='llama',
            context_length=512,
            gpu_layers=0
        )
        print("AI model loaded successfully")
        return model
    except Exception as e:
        print(f"Failed to load AI model: {str(e)}")
        return None

def clean_ai_response(response):
    """Clean and format AI response."""
    cleaned = re.sub(r'[^\w\s\-\.]', '', response)
    cleaned = ' '.join(cleaned.split())
    
    if not cleaned or len(cleaned.split()) < 2:
        return None
    
    words = cleaned.split()[:10]
    cleaned = ' '.join(words)
    
    cleaned = cleaned.capitalize()
    if not cleaned.endswith('.'):
        cleaned += '.'
    
    return cleaned

def get_default_description(table_name, column_name, data_type):
    """Generate a meaningful default description based on column properties."""
    if column_name.endswith('_id'):
        related_entity = column_name[:-3].replace('_', ' ').title()
        return f"Reference to {related_entity} table."
    elif column_name.endswith('_at'):
        action = column_name[:-3].replace('_', ' ')
        return f"Timestamp of {action} action."
    elif column_name == 'id':
        return "Primary key identifier."
    elif column_name == 'created_at':
        return "Record creation timestamp."
    elif column_name == 'updated_at':
        return "Last update timestamp."
    elif column_name == 'deleted_at':
        return "Soft deletion timestamp."
    elif column_name == 'name':
        return f"{table_name.rstrip('s').title()} name."
    elif column_name == 'description':
        return f"{table_name.rstrip('s').title()} description."
    elif column_name == 'email':
        return "Email address."
    elif column_name == 'password':
        return "Hashed password."
    elif column_name == 'status':
        return f"Current {table_name.rstrip('s')} status."
    
    words = column_name.replace('_', ' ').split()
    if len(words) > 1:
        return f"{' '.join(words).capitalize()}."
    else:
        return f"The {column_name.replace('_', ' ')} of the {table_name.rstrip('s')}."

def generate_ai_description(model, table_name, column_name, data_type):
    if model is None:
        return get_default_description(table_name, column_name, data_type)
        
    try:
        prompt = f"""<|im_start|>system
You are a technical writer. Write extremely concise database column descriptions.
Rules:
- Maximum 5 words
- Be technical and precise
- No special characters
- No quotes
- Always provide meaningful description
<|im_end|>
<|im_start|>user
Write technical description for:
Table: {table_name}
Column: {column_name}
Type: {data_type}
<|im_end|>
<|im_start|>assistant"""
        
        response = model(prompt, 
                        max_new_tokens=20,
                        temperature=0.1,
                        top_k=1,
                        stop=["<|im_end|>", "\n"])
        
        cleaned_response = clean_ai_response(response)
        if cleaned_response:
            return cleaned_response
        
        return get_default_description(table_name, column_name, data_type)
        
    except Exception as e:
        print(f"AI generation failed for {table_name}.{column_name}: {str(e)}")
        return get_default_description(table_name, column_name, data_type) 