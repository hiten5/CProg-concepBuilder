while True:
    ip=input('enter a amount to withdraw')
    try:
        num=float(ip)
        break
    except:
        print('please enter a number')
        continue                            #continue will get execution to start from strting of loop

print('your request to withdraw', num, '$ is accepted')
