
import openai

openai.api_key = "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"

start_sequence="\nAI: "
restart_sequence="\nHuman: "
while True:
 ask=input("Enter : ")
 if ask=="break":
   print("Thankyou!  ")
 else: 
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=ask,
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=['Human :',"AI:"]
    )
print(response)