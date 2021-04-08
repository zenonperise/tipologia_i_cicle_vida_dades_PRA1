{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "controlling-agriculture",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'null' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-51-344a74cc8ddd>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mcsv\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mpandas\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0;32mfrom\u001b[0m \u001b[0mmain\u001b[0m \u001b[0;32mimport\u001b[0m \u001b[0mdf\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Importem llibreries per carragar les variables i poder crear un arxiu csv amb les dades obtingudes\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m/mnt/c/Users/vidalot/Desktop/main.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      3\u001b[0m   {\n\u001b[1;32m      4\u001b[0m    \u001b[0;34m\"cell_type\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;34m\"code\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 5\u001b[0;31m    \u001b[0;34m\"execution_count\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mnull\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      6\u001b[0m    \u001b[0;34m\"id\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;34m\"offshore-session\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      7\u001b[0m    \u001b[0;34m\"metadata\"\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;34m{\u001b[0m\u001b[0;34m}\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'null' is not defined"
     ]
    }
   ],
   "source": [
    "import csv\n",
    "import pandas as pd\n",
    "from main import df\n",
    "\n",
    "print(\"Importem llibreries per carragar les variables\")\n",
    "\n",
    "\n",
    "\n",
    "with open('output.csv', 'w+') as f:\n",
    "    f.write(df)\n",
    "    \n",
    "print(\"S'ha creat un arxiu csv output.csv amb les dades obtingudes\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "portuguese-queen",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "grand-conservative",
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
