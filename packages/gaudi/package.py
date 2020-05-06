from spack import *

class Gaudi(Package):
    """Gaudi framework."""
    homepage = "https://gaudi.cern.ch"
    url      = "https://gaudi.cern.ch"

    version('v27r1', git='https://gitlab.cern.ch/gaudi/Gaudi.git', tag='v27r1')
    version('v28r0', git='https://gitlab.cern.ch/gaudi/Gaudi.git', tag='v28r0')
    version('v28r1', git='https://gitlab.cern.ch/gaudi/Gaudi.git', tag='v28r1')

    depends_on("python")
    depends_on("root")
    depends_on("py-qmtest")
    depends_on("clhep")
    depends_on("boost")
    depends_on("cppunit")
    depends_on("aida")
    depends_on("tbb")
    depends_on("gperftools")
    depends_on("heppdt")

    def install(self, spec, prefix):
        options = []
        options.extend(std_cmake_args)

        build_directory = join_path(self.stage.path, 'spack-build')
        source_directory = self.stage.source_path

        if '+debug' in spec:
            options.append('-DCMAKE_BUILD_TYPE:STRING=Debug ')

	#options.append("-DCMAKE_TOOLCHAIN_FILE=" + source_directory +"/toolchain.cmake")

        with working_dir(build_directory, create=True):
            import os
            cmake(source_directory , *options)
            make(" VERBOSE=1")
            make("install")

