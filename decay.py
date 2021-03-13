{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "from random import random\n",
    "from numpy import arange\n",
    "from pylab import plot, xlabel, ylabel, show\n",
    "\n",
    "\n",
    "NT1 = 1000\n",
    "NPb = 0\n",
    "tau = 3.053*60\n",
    "h = 1.0\n",
    "p = 1 - 2**(-h/tau)\n",
    "tmax = 1000\n",
    "\n",
    "tpoints = arange(0.0,tmax,h)\n",
    "T1points = []\n",
    "Pbpoints = []\n",
    "\n",
    "for t in tpoints:\n",
    "    T1points.append(NT1)\n",
    "    Pbpoints.append(NPb)\n",
    "    \n",
    "    decay = 0\n",
    "    for i in range(NT1):\n",
    "        if random()<p:\n",
    "            decay+=1\n",
    "    NT1 -= decay\n",
    "    NPb += decay\n",
    "    \n",
    "plot(tpoints, T1points)\n",
    "plot(tpoints, Pbpoints)\n",
    "xlabel(\"Time\")\n",
    "ylabel(\"number of atoms\")\n",
    "show()"
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
