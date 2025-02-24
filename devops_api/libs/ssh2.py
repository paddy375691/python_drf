import paramiko

# 配置远程服务器的信息
hostname = '192.168.201.113'  # 远程服务器的 IP 地址
port = 22  # SSH 端口，默认为 22
username = 'root'  # 远程服务器的用户名
private_key_path = 'D:\\id_rsa'  # 私钥文件的路径

# 加载私钥
private_key = paramiko.RSAKey.from_private_key_file(private_key_path)

# 创建 SSH 客户端
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 自动接受远程服务器的 SSH 密钥

try:
    # 连接到远程服务器
    ssh.connect(hostname, port, username, pkey=private_key)
    print("SSH 连接成功！")

    # 执行命令
    stdin, stdout, stderr = ssh.exec_command('ls -l')
    print("命令输出：")
    print(stdout.read().decode())

except Exception as e:
    print(f"SSH 连接失败！错误：{e}")

finally:
    # 关闭连接
    ssh.close()