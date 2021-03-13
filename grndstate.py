{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "E =  134.28637169369105 eV\n"
     ]
    }
   ],
   "source": [
    "from numpy import array, arange\n",
    "\n",
    "m = 9.1094e-31\n",
    "hbar = 1.0546e-34\n",
    "e = 1.6022e-19\n",
    "L = 5.2918e-11\n",
    "N = 1000\n",
    "h = L/N\n",
    "\n",
    "def V(x):\n",
    "    return 0.0\n",
    "\n",
    "def f(r,x,E) :\n",
    "    psi = r[0]\n",
    "    phi = r[1]\n",
    "    fpsi =phi\n",
    "    fphi = (2*m/hbar**2)*(V(x)-E)*psi\n",
    "    return array([fpsi,fphi], float)\n",
    "\n",
    "def solve(E) :\n",
    "    psi = 0.0\n",
    "    phi = 1.0\n",
    "    r = array([psi,phi], float)\n",
    "    \n",
    "    for x in arange(0,L,h):\n",
    "        k1 = h*f(r,x,E)\n",
    "        k2 = h*f(r+0.5*k1,x+0.5*h,E)\n",
    "        k3 = h*f(r+0.5*k2,x+0.5*h,E)\n",
    "        k4 = h*f(r+k3,x+h,E)\n",
    "        r += (k1+2*k2+2*k3 + k4)/6\n",
    "        \n",
    "    return r[0]\n",
    "\n",
    "E1 = 0.0\n",
    "E2 = e\n",
    "psi2 = solve(E1)\n",
    "\n",
    "target = e/1000\n",
    "while abs(E1-E2) > target:\n",
    "    psi1,psi2 = psi2,solve(E2)\n",
    "    E1,E2 = E2,E2-psi2*(E2-E1)/(psi2-psi1)\n",
    "    \n",
    "print(\"E = \", E2/e, \"eV\")\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
