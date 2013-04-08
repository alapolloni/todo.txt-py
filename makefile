#this just make the todo.exe and copies it to the base directory

todotxtexe: todo.py
	"C:\Python27\pyinstaller-2.0\pyinstaller.py" -i Icon.ico -F -y -o . todo.py	
	cp dist/todo.exe . 
