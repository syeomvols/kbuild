from setuptools import setup, find_packages, Extension
from setuptools.command.build_ext import build_ext
import os
from numpy import get_include

# Define the Extension for the Fortran script
class f2py_Extension(Extension):

    def __init__(self, PackageName, sourcedirs):
        Extension.__init__(self, PackageName, sources=[])
        self.sourcedirs = [os.path.abspath(sourcedir) for sourcedir in sourcedirs]
        self.dirs = sourcedirs
        self.include_dirs=[get_include()]
        self.packages=find_packages(where=PackageName)

        

class f2py_Build(build_ext):
    
    def run(self):
        # Compile Fortran script using f2py and create shared object file
        for ext in self.extensions:
            self.build_extension(ext)

        # Copy the shared object file to the build directory
        
        lib_name = self.get_ext_filename('fibby/fib')
        
        build_lib = os.path.abspath(self.build_lib)
        lib_path = os.path.join(build_lib, lib_name)
        self.copy_file(lib_name, lib_path)

        # Continue with the build process
        build_ext.run(self)
        
    def build_extension(self, ext):
        # compile
        for ind,to_compile in enumerate(ext.sourcedirs):
            module_loc = os.path.split(ext.dirs[ind])[0]
            module_name = os.path.split(to_compile)[1].split('.')[0]
            os.system(f'cd {module_loc};f2py -c {to_compile} -m {module_name}')

setup(
    name='fibby',
    version='1.0.0',
    packages=find_packages(),
    install_requires=['numpy'],
    ext_modules=[f2py_Extension('fibby',['fibby/fib.f90'])],  # Include the Fortran extension
    entry_points={
        'console_scripts': [
            'fibby = fibby.__main__:main'
        ]
    },
    cmdclass=dict(build_ext=f2py_Build),  # Use custom build_ext
)
