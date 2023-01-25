FROM python

WORKDIR /opt/network-scanner
RUN apt update && apt install net-tools nmap -y

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]
