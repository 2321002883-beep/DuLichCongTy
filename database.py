import pymysql


def get_connection():

    conn = pymysql.connect(

        host="mysql-29c20b51-sv-c4e0.d.aivencloud.com",

        port=27959,

        user="avnadmin",

        password="AVNS_4fem3OwTQy5llb1MK9y",

        database="company",

        ssl={
            "ca": "ca.pem"
        }

    )

    return conn
