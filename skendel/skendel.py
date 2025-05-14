import tkinter as tk
#criar a porra toda
#########################################
janela = tk.Tk()
janela.resizable(False, False)
janela.geometry('1250x900')
janela.title("slk")

printchange = tk.BooleanVar()
printchange.set(True)
tabular = tk.BooleanVar()
tabular.set(True)

#Código que roda quando eu quero
#########################################



def analise(exp, text):
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

    i = 0
    ruleQ = rules[:]
    while i < len(text):
        if ruleQ[0][0] == "#":
            print("textMatch")
        elif ruleQ[0][0] == "t":
            print("tilMatch")
        elif ruleQ[0][0] in "0123456789":
            print("quantityMatch")
        elif ruleQ[0][0] == "i":
            print("maxMatch")
        ruleQ.pop(0)
        i += 1

    return(", ".join(rules))


#funcoes tkinter
#########################################
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

#Detalhes, textos
#########################################
textoinput = tk.Label(janela, text="Expressão:")
textoinput.grid(row=0, column=1, padx=10, pady=10)
textoinput2 = tk.Label(janela, text="Outs:")
textoinput2.grid(row=0, column=2, padx=10, pady=10)

#Caixas de input, output
#########################################
output = tk.Text(janela, height=50, width=75, state=tk.DISABLED)
output.grid(row=1, column=2, padx=10, pady=10)

input = tk.Text(janela, height=1, width=75)
input.grid(row=0, column=1, padx=10, pady=10)
input.bind("<KeyRelease>", atualizar)

text = tk.Text(janela, height=50, width=75)
text.grid(row=1, column=1, padx=10, pady=10)

#necessario
#########################################
janela.mainloop()