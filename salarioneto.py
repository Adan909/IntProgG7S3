salario_bruto= float(input("Ingrese el salario bruto: "))
IR= salario_bruto*0.10
SS= salario_bruto*0.05
fp= salario_bruto*0.03
salario_neto= salario_bruto-(IR+SS+fp)
desc_tot= (IR+SS+fp)
print("El salario bruto es de: ", salario_bruto, " los descuentos totales son de: ", desc_tot, " y su salario neto es de: ", salario_neto)

