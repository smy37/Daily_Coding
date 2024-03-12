import openai
import json

##openai.api_key = "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"
#openai.api_key = "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"
openai.api_key = "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"

# def get_cur_element(elem, unit="fahrenheiet"):
#     if "beam" in elem.lower():
#         return json.dumps({"Element": "Beam", "Length": 20, "unit": unit})
#     elif "section" in elem.lower():
#         return json.dumps({"Element": "Beam", "Length": 20, "unit": unit})
#     elif "column" in elem.lower():
#         return json.dumps({"Element": "Beam", "Length": 20, "unit": unit})
#
#
# def run_conversation():
#     messages = [{"role": "user", "content": "What's the element like Beam, Section, Col"}]
#     tools = [
#         {
#             "type": "function",
#             "function": {
#                 "name": "get current element",
#                 "description": "Get the current element in a given location",
#                 "parameters": {
#                     "type": "object",
#                     "properties": {
#                         "location": {
#                             "type": "string",
#                             "description": "The composite of structure, e.g. beam, element, section"
#                         },
#                         "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
#                     },
#                     "required": ["location"],
#                 },
#             },
#         }
#     ]
#
#     response = openai.ChatCompletion.create(
#         model="gpt-4",
#         messages=messages,
#         tools=tools,
#         tool_choice="auto",
#     )
#
#     response_message = response.choices[0].message
#     tool_calls = response_message.tool_calls
#
#     if response_message.get("function_call"):
#         available_functions = {
#             "get_cur_elem": get_cur_element
#         }
#
# print(run_conversation())

import openai
import json

def get_current_weather(location, unit="fahrenheit"):
    weather_info = {
        "location": location,
        "temperature": "24",
        "unit": unit,
        "forecast": ["sunny", "windy"],
    }
    return json.dumps(weather_info)

messages = [{"role": "user", "content": "지금 서울날씨를 섭씨로 알려줘."}]
functions = [
    {
        "name": "get_current_weather",
        "description": "특정 지역의 날씨를 알려줍니다.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "지역이름 eg. 서울, 부산, 제주도",
                },
                "unit": {"type": "string", "enum": ["섭씨", "화씨"]},
            },
            "required": ["location"],
        },
    }
]
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=messages,
    functions=functions,
    function_call="auto",
    )
response_message = response["choices"][0]["message"]

print(response_message)

if response_message.get("function_call"):
    # Note: the JSON response may not always be valid; be sure to handle errors
    available_functions = {
        "get_current_weather": get_current_weather,
    }
    function_name = response_message["function_call"]["name"]
    fuction_to_call = available_functions[function_name]
    function_args = json.loads(response_message["function_call"]["arguments"])
    function_response = fuction_to_call(
        location=function_args.get("location"),
        unit=function_args.get("unit"),
    )

    messages.append(response_message)
    messages.append(
        {
            "role": "function",
            "name": function_name,
            "content": function_response,
        }
    )
    second_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
    )  # get a new response from GPT where it can see the function response


    json_data = json.dumps(second_response, ensure_ascii=False)
    print("What the Hell?")
    print(second_response)
    print("Nice!")