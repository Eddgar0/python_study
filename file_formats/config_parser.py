import configparser

radio_controls = {
    'audio': {'max_volumen':75, 'canal':'estereo'},
    'radio': {'banda':'FM', 'ecualizador':'Si', 'entrada':'radio'}
}

parser = configparser.ConfigParser()
parser.read_dict(radio_controls)

with open('radio.cfg', 'w') as f:
    parser.write(f)

with open('radio.cfg') as f:
    print(f.read())


parser.read('radio.cfg')
print(parser.sections())
parser2 = configparser.ConfigParser()
parser2.read('ansible_host.cfg')