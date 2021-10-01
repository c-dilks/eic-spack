from spack import *


class Eicd(CMakePackage):
    """A podio based data model for the EIC."""

    homepage = "https://eicweb.phy.anl.gov/EIC/eicd"
    url      = "https://eicweb.phy.anl.gov/EIC/eicd/-/archive/v0.2.0/eicd-v0.2.0.tar.gz"
    git      = "https://eicweb.phy.anl.gov/EIC/eicd.git"
    list_url = "https://eicweb.phy.anl.gov/EIC/eicd/-/tags"

    maintainers = ['wdconinc']

    version('master', branch='master', preferred=True)
    version('0.8.0', sha256='140b191c7bb64d5fc7c039b646ade9ecfeb00509ad19eb04917cd6f2ace3b1d1')
    version('0.7.0', sha256='12458ed06d3f7d3f17852637d8b7f6c406e8ffb24b487d690be81d342a0c0e75')
    version('0.6.0', sha256='e44a7535ce0e94bfa4df0676ffc3af90b9ed90626cb4b524860576848bfc9ed7')
    version('0.5.0', sha256='597b22a7d8b1ba9d1f3c0facee8f8df95cc4d4baa9d9c7f1a624dfa13b48751b')
    version('0.2.0', sha256='3e52e19bdfbda67454786080db678107a00b932b4cf26bfd95bbf764cc1f7fc9')
    version('0.1.0', sha256='814eec1b6c27e46fdedfd3f42d846366c6170c3b1c7b5225c28465d0861b612c')

    depends_on('podio@0.11.0:')
    depends_on('root')
