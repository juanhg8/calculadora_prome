import tkinter as tk
from tkinter import messagebox

NOTA_MINIMA = 6.0

entry_nombre = None
entry_cantidad = None
frame_principal = None      # marco principal donde se ubican los campos iniciales
frame_materias = None
btn_calcular = None
btn_continuar = None
btn_reiniciar = None
materias_entries = []
notas_entries = []


def iniciar_formulario():
    global entry_nombre, entry_cantidad, btn_continuar

    frame_principal.pack(padx=10, pady=10)

    tk.Label(frame_principal, text="Nombre del estudiante:").grid(row=0, column=0, sticky="w")
    entry_nombre = tk.Entry(frame_principal)
    entry_nombre.grid(row=0, column=1)

    tk.Label(frame_principal, text="Cantidad de materias:").grid(row=1, column=0, sticky="w")
    entry_cantidad = tk.Entry(frame_principal)
    entry_cantidad.grid(row=1, column=1)

    btn_continuar = tk.Button(frame_principal, text="Ingresar materias", command=crear_campos)
    btn_continuar.grid(row=2, column=0, columnspan=2, pady=(5, 0))


def crear_campos():
    global materias_entries, notas_entries, frame_materias, btn_calcular

    try:
        cantidad = int(entry_cantidad.get())
        if cantidad <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número entero positivo para la cantidad.")
        return

    entry_nombre.config(state="disabled")
    entry_cantidad.config(state="disabled")
    btn_continuar.config(state="disabled")

    materias_entries = []
    notas_entries = []

    frame_materias = tk.Frame(root)
    frame_materias.pack(padx=10, pady=10)

    for i in range(cantidad):
        tk.Label(frame_materias, text=f"Materia #{i+1}:").grid(row=i, column=0, sticky="w")
        m = tk.Entry(frame_materias)
        m.grid(row=i, column=1)
        materias_entries.append(m)

        tk.Label(frame_materias, text="Nota:").grid(row=i, column=2, sticky="w")
        n = tk.Entry(frame_materias)
        n.grid(row=i, column=3)
        notas_entries.append(n)

    btn_calcular = tk.Button(root, text="Calcular promedio", command=calcular_promedio)
    btn_calcular.pack(pady=(5, 0))


def calcular_promedio():
    global btn_reiniciar

    nombre = entry_nombre.get().strip()
    total = 0.0

    for m_entry, n_entry in zip(materias_entries, notas_entries):
        materia = m_entry.get().strip()
        try:
            nota = float(n_entry.get())
            if nota < 0 or nota > 10:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", f"Nota inválida para {materia or 'una materia'}.")
            return
        total += nota

    cantidad = len(notas_entries)
    promedio = total / cantidad if cantidad > 0 else 0.0
    estado = "APROBADO" if promedio >= NOTA_MINIMA else "REPROBADO"

    messagebox.showinfo("Resultado",
                        f"Estudiante: {nombre}\n"
                        f"Promedio: {promedio:.2f}\n"
                        f"Estado: {estado}")

    # mostrar botón para reiniciar
    btn_reiniciar = tk.Button(root, text="Nuevo estudiante", command=reiniciar)
    btn_reiniciar.pack(pady=(5, 0))
    btn_calcular.config(state="disabled")


def reiniciar():
    global frame_materias, btn_calcular, btn_reiniciar, materias_entries, notas_entries

    entry_nombre.config(state="normal")
    entry_cantidad.config(state="normal")
    entry_nombre.delete(0, tk.END)
    entry_cantidad.delete(0, tk.END)
    btn_continuar.config(state="normal")

    if frame_materias is not None:
        frame_materias.destroy()
        frame_materias = None

    if btn_calcular is not None:
        btn_calcular.destroy()
        btn_calcular = None

    if btn_reiniciar is not None:
        btn_reiniciar.destroy()
        btn_reiniciar = None

    materias_entries = []
    notas_entries = []


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Calculadora de Promedios")

    frame_principal = tk.Frame(root)
    iniciar_formulario()

    root.mainloop()
