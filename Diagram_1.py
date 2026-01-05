{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "177cdfa1-e5ef-48c3-815e-157effce23d5",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'diagrams'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[1], line 1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mdiagrams\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m Diagram\n\u001b[1;32m      2\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mdiagrams\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01maws\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mcompute\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m EC2\n\u001b[1;32m      4\u001b[0m \u001b[38;5;28;01mwith\u001b[39;00m Diagram(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mTest Diagram\u001b[39m\u001b[38;5;124m\"\u001b[39m):\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'diagrams'"
     ]
    }
   ],
   "source": [
    "from diagrams import Diagram\n",
    "from diagrams.aws.compute import EC2\n",
    "\n",
    "with Diagram(\"Test Diagram\"):\n",
    "    EC2(\"Server\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ac9c5321-8b70-4004-ba71-87ceb2f3b0cb",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.13.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
