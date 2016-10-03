# coding=UTF-8

from ISO8583.ISO8583 import ISO8583

message = ISO8583()
message.setMTI('0800')
message.setBit(3, '300000')
message.setBit(24, '045')
message.setBit(41, '11111111')
message.setBit(42, '222222222222222')
message.setBit(62, '--Mensagem enviada do cliente--')
message.setBit(63, '0810')

print '\nNetwork message: \n%s\n' % message.getNetworkISO()

for v in message.getBitsAndValues():
  print '\t Bit: %s type: %s value: %s' % (v['bit'],v['type'],v['value'])

print '\n'