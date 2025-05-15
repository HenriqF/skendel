import tkinter as tk
import ast

janela = tk.Tk()
janela.resizable(False, False)
janela.geometry('1250x900')
janela.title("slk")

printchange = tk.BooleanVar()
printchange.set(True)
tabular = tk.BooleanVar()
tabular.set(True)


def analise(exp, text):
    biblio = ""
    with open("biblioteca.txt", "r") as file:
        biblio = ast.literal_eval(file.read())

    exp = " "+exp+" "
    rules = []
    i = 0
    while i < len(exp):
        if exp[i] == "<" and exp[i-1] != "#":
            rule = ""
            tkns = "#<>"
            i += 1
            while exp[i] != ">":
                if exp[i] == "#" and exp[i+1] in tkns:
                    rule += exp[i+1]
                    i += 2
                else:
                    rule += exp[i]
                    i += 1
            rules.append(rule)
        i += 1

    result = ""
    currentExp = ""
    sucessFlag = True

    j = -1
    i = 0
    ruleQ = []
    while j <= len(text):
        if ruleQ == []:
            if sucessFlag == False:
                j += 1
                i = j
                sucessFlag = True
            else:
                j = i
                result += currentExp
            ruleQ = rules[:]
            currentExp = ""
        ruleC = ruleQ[0]

        if ruleC[0] == "#": #text match (qualquer coisa que vier depois de "#")
            comprimento = len(ruleC[1:])
            if text[i:i+comprimento] == ruleC[1:]:
                currentExp+=text[i:i+comprimento]
                i += comprimento-1
            else:
                currentExp = ""
                ruleQ == []
                sucessFlag = False

        if ruleC[0] in "dua": #digit/char match (n? que vier depois da letra)
            compCharMap = biblio[0] if ruleC[0] == "d" else biblio[1] if ruleC == "u" else biblio[2]
            comprimento = len(ruleC[1:])
            if comprimento > 0:
                analise = text[i:i+comprimento]
                analisado = ""
                for char in analise:
                    if char in compCharMap:
                        analisado += char
                
                print(analisado, analise)
                if analisado == analise:
                    currentExp+=text[i:i+comprimento]
                    i += comprimento-1
                else:
                    currentExp = ""
                    ruleQ == []
                    sucessFlag = False

        ruleQ.pop(0)
        i += 1
    return(result)


###############################################
def enviar():
    user_text = text.get("1.0", tk.END).strip()
    user_exp = input.get("1.0", tk.END).strip()
    result = analise(user_exp, user_text)
    output.config(state=tk.NORMAL)
    output.delete("1.0", tk.END)
    output.insert(tk.END, str(result))
    janela.update()

def atualizar(*args):
    enviar()

#################################################################
textoinput2 = tk.Label(janela, text="Resultado:")
textoinput2.grid(row=0, column=2, padx=10, pady=10)

output = tk.Text(janela, height=50, width=75, state=tk.DISABLED)
output.grid(row=1, column=2, padx=10, pady=10)

input = tk.Text(janela, height=1, width=75)
input.grid(row=0, column=1, padx=10, pady=10)
input.bind("<KeyRelease>", atualizar)

text = tk.Text(janela, height=50, width=75)
text.grid(row=1, column=1, padx=10, pady=10)
text.bind("<KeyRelease>", atualizar)

text.insert(tk.END, '1234av')

janela.mainloop()