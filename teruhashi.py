file = input("file name: ")
'''
extension = ('png', 'jpg', 'jpeg', 'gif')


for i in extension:
    if file.endswith(i) == True:#
        print('accepted')
        break
print('invalid file name')
'''
if file.endswith('png') or file.endswith('jpg') or file.endswith('jpeg') or file.endswith('gif'):
    print('accepted')
else:
    print('invalid file name')
