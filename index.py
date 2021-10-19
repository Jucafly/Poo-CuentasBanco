class Cuenta:

     def __init__(self,numero_cuenta,saldo,interes_anual):
         self.numero_cueta = numero_cuenta
         self.saldo = saldo
         self.interes_anual = interes_anual

     def DarSaldo(self):
         return self.saldo
    
     def DarInteres(self):
         return self.interes_anual
     
     def ModSaldo(self,s):
         self.saldo = s

     def ModInteres(self,i):
         self.interes_anual = i

     def Ingreso(self,cantidad):
         self.saldo = self.saldo + cantidad
     
     def Reingreslo(self,r):
         if (r > self.saldo):
             return False
         else:
             self.saldo = self.saldo - r
             return True

     def MostrarDatos(self):
         print('Numero de cuenta: {} '.format(self.numero_cueta))
         print('El Saldo es de: {} \n' .format(self.saldo))

def main():     #N.Cuenta Saldo Intereses
    cc = Cuenta(24316622,12000,3)
    cc.MostrarDatos()
    cc.ModSaldo(10000)
    cc.ModInteres(2)
    cc.MostrarDatos()
    cc.Ingreso(1200)
    cc.MostrarDatos()
    
if __name__ == "__main__":
    main()

         