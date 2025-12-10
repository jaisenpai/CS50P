def extension_output(ans) :
    ans = ans.lower().strip().split('.')
    if ans[-1] == 'jpg' or ans[-1] == 'jpeg':
        print ('image/jpeg')
    elif ans[-1] == 'gif' :
        print ('image/gif')
    elif ans[-1] == 'png' :
        print ('image/png')
    elif ans[-1] == 'pdf' :
        print ('application/pdf')
    elif ans[-1] == 'txt' :
        print ('text/plain')
    elif ans[-1] == 'zip' :
        print ('application/zip')

    else :
        print ('application/octet-stream')

x_in = input('file name: ')
extension_output(x_in)
