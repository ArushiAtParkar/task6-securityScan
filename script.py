import os
import hashlib

# Embedded credentials (do not do this)
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

def insecure_command(user_input):
    # Command injection vulnerability
    os.system("echo " + user_input)

def insecure_sql(user_input):
    # SQL injection vulnerability
    query = "SELECT * FROM users WHERE name = '%s'" % user_input
    print("Executing query:", query)
    # Imagine this executes the query on a real database

def insecure_hash(password):
    # Use of insecure MD5 hash
    return hashlib.md5(password.encode()).hexdigest()

def directory_traversal(filename):
    # Directory traversal vulnerability
    with open("/tmp/" + filename, "r") as f:
        return f.read()

if __name__ == "__main__":
    # Example usage (do not use in production)
    insecure_command("test; ls /")
    insecure_sql("admin' OR '1'='1")
    print(insecure_hash("password123"))
    print(directory_traversal("../../etc/passwd"))
