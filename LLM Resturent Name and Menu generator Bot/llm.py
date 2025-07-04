from langchain_community.llms import Ollama 
from langchain.prompts import PromptTemplate 
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain, SequentialChain

llm = Ollama(model="deepseek-r1:1.5b")



def LLM(items):
    prompt_templates_name = PromptTemplate(
    input_variables = ["cuisine"],
    template = 'I want to start a resturent {cuisine} foods. sugges the professioanl name for that.'
    )
    Name_Chain = LLMChain(llm = llm, prompt = prompt_templates_name, output_key="Resturent_Name")
    

    prompt_templates_menu = PromptTemplate(
        input_variables = ["cuisine"],
        template = 'Suggest the some menu items for the {Resturent_Name} Returen with seperated commas'
    )
    Menu_Chain = LLMChain(llm = llm, prompt = prompt_templates_menu, output_key="menu_items")

    chain = SequentialChain(
        chains=[Name_Chain, Menu_Chain],
        input_variables=["cuisine"],
        output_variables=["Resturent_Name", "menu_items"],  

    )

    response = chain({'cuisine':items})

    return response

if __name__ == "__main__":
    print(LLM("Sri Lankan"))
