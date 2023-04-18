#!/usr/bin/env python3
import time
import traceback
import tkinter as tk
import random
from tkinter.messagebox import showerror

class SubleqMachine:
    def __init__(self):
        self.memory = [0] * 256
        self.pc = 0

    def load_program(self, program):
        for i in range(len(program)):
            self.memory[i] = program[i]

    def reset(self):
        self.pc = 0

    def step(self):
        a = self.memory[self.pc]
        b = self.memory[(self.pc + 1) % 256]
        c = self.memory[(self.pc + 2) % 256]
        while a < 0:
            a += 256
        while b < 0:
            b += 256
        while c < 0:
            c += 256
        a = a % 256
        b = b % 256
        c = c % 256
        self.memory[b] = self.memory[b] - self.memory[a]
        if self.memory[b] <= 0:
            self.pc = c
        else:
            self.pc = (self.pc + 3) % 256

class SubleqGUI:
    def __init__(self):
        self.machine = SubleqMachine()
        
        self.root = tk.Tk()
        self.root.title("8-bit Subleq Machine")
        
        self.code_text = tk.Text(self.root, height=20, width=40)
        self.code_text.pack(side=tk.LEFT, padx=10, pady=10)

        frame = tk.Frame(self.root)
        frame.pack(side=tk.TOP, pady=5)
        self.load_button = tk.Button(frame, text="Load", command=self.load_program)
        self.load_button.pack(side=tk.LEFT, pady=5)
        self.step_button = tk.Button(frame, text="Step", command=self.step_program)
        self.step_button.pack(side=tk.LEFT, pady=5)

        self.sim_button = tk.Button(frame, text="Animate", command=self.sim_program)
        self.sim_button.pack(side=tk.LEFT, pady=5)
        
        self.run_button = tk.Button(frame, text="1000 Steps", command=self.run_program)
        self.run_button.pack(side=tk.LEFT, pady=5)
        
        self.reset_button = tk.Button(frame, text="Reset", command=self.reset_program)
        self.reset_button.pack(side=tk.LEFT, pady=5)

        self.random_button = tk.Button(frame, text="Random", command=self.random_program)
        self.random_button.pack(side=tk.LEFT, pady=5)

        frame = tk.Frame(self.root)
        frame.pack(side=tk.TOP, pady=5)
        self.pc_label = tk.Label(frame, text="PC: 0")
        self.pc_label.pack(side=tk.TOP, pady=5)

        frame = tk.Frame(self.root)
        frame.pack(side=tk.TOP, pady=5)
        cells = []
        if True:
            e = tk.Label(frame, text="")
            self.orig_color = e.cget("background")
            e.grid(row=0, column=0)
            for j in range(10):
                e = tk.Label(frame, text="   %d  " % j)
                e.configure(bg="light gray")
                e.grid(row=0, column=j+1)
        for i in range(26):
            e = tk.Label(frame, text="%03d" % (i*10))
            e.configure(bg="light gray")
            e.grid(row=i+1, column=0)
            for j in range(10):
                e = tk.Label(frame, text="0")
                e.grid(row=i+1, column=j+1)
                cells.append(e)
        self.cells = cells
        
        self.update_memory_display()
        
        self.root.mainloop()

    def load_impl (self):
        text = self.code_text.get("1.0", tk.END)
        memory = [0] * 256
        addr = 0
        for no, line in enumerate(text.split('\n')):
            off = line.find('#')
            if off >= 0:
                line = line[:off]
            line = line.strip()
            if len(line) == 0:
                continue
            off = line.find(':')
            if off >= 0:
                addr = int(line[:off])
                line = line[(off+1):]
                line = line.strip()
            if len(line) == 0:
                continue
            a, b, c = [int(x) for x in line.split(' ')]
            memory[addr] = a
            memory[addr+1] = b
            memory[addr+2] = c
            addr += 3
        return memory
    
    def load_program (self):
        # compile
        try:
            mem = self.load_impl()
        except:
            traceback.print_exc()
            showerror("Error", "BAD")
            return
        self.machine.load_program(mem)
        self.machine.reset()
        self.update_memory_display()
        pass

    def sim_program(self, n=100):
        for _ in range(n):
            self.step_program()
            self.root.update()
            time.sleep(0.2)
    
    def run_program(self, n=1000):
        for _ in range(n):
            self.machine.step()
        self.update_memory_display()
    
    def step_program(self):
        self.machine.step()
        self.update_memory_display()

    def reset_program(self):
        self.machine.reset()
        self.update_memory_display()

    def random_program (self):
        prog = [random.randint(0, 255) for _ in range(256)]
        self.machine.pc = random.randint(0, 255)
        self.machine.load_program(prog)
        self.update_memory_display()

    
    def update_memory_display(self):
        pc = self.machine.pc
        self.pc_label.config(text="PC: %d" % pc)
        for i in range(len(self.machine.memory)):
            text = "%d" % self.machine.memory[i]
            pad = 6 - len(text)
            left = pad//2
            pad -= left
            text = (' ' * left) + text + (' ' * pad)
            self.cells[i].config(text="%d" % self.machine.memory[i], bg=self.orig_color)
        self.cells[pc].config(bg='red')
        self.cells[(pc+1)%256].config(bg='red')
        self.cells[(pc+2)%256].config(bg='red')

gui = SubleqGUI()
