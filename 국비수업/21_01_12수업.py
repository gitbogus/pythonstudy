import cx_Oracle as oci

# Oracle 서버와 연결(Connection 맺기) 11.2.0\server\bin\oci.dll을 로드
#conn = oci.connect('system/암호@localhost:1521/xe')
conn = oci.connect('system/shtkd159!@@localhost:1521/xe')
#conn = oci.connect('system','oracle','localhost:1521/xe')

# Connection 확인
print(conn.version)
