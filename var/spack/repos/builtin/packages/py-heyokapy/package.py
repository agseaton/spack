# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyHeyokapy(PythonPackage):
    """heyoka.py is a python library for integration of ODEs via Taylor’s method"""

    homepage = "https://bluescarni.github.io/heyoka.py"
    url = "https://github.com/bluescarni/heyoka.py/archive/refs/tags/v5.1.0.tar.gz"

    # A list of GitHub accounts to notify when the package is updated.
    maintainers("bluescarni", "agseaton")

    # SPDX identifier of the project's license.
    license("MPL-2.0")

    version("5.1.0", sha256="8e0f4adeb5fc2652d6bd9cd31605e5807ecd6c58096a7d1f3623d864c0dbdcac")

    variant("mppp", default=False, description="enable features relying on the mp++ library")

    # Add in a pyproject.toml file using scikit-build-core as a build backend
    # to enable a standardised build from source.
    patch("pyproject.toml.patch")

    # Dependencies

    # Build backend
    depends_on("py-scikit-build-core", type="build")
    depends_on("cmake@3.18:", type="build")

    # Other build dependencies
    depends_on("python@3.5:3.11", when="@0.2:3.0", type=('build', 'run'))
    depends_on("python@3.5:3.12", when="@3.1:", type=('build', 'run'))
    depends_on("py-numpy@1.22:", type=('build', 'run'))
    depends_on("py-pybind11@2.10:", type=('build', 'run'))
    # TODO: Check if this version is actually necessary
    depends_on("boost@1.69:", type=('build', 'run'))
    depends_on("fmt@9:10", when="@0.5:", type=('build', 'run'))
    depends_on("intel-tbb@2021.4.0:", type=('build', 'run'))

    depends_on("mppp@1 +serialization +fmt +mpfr +mpc", when="+mppp",
               type=('build', 'run'))

    # Additional dependencies.

    # Heyoka C++ library
    # TODO: Can this be made more concise?
    with when("+mppp"):
        depends_on("heyoka@5.1+mppp", when="@5.1")
        depends_on("heyoka@5.0+mppp", when="@5.0")
        depends_on("heyoka@4.0+mppp", when="@4.0")
        depends_on("heyoka@3.2+mppp", when="@3.2")
        depends_on("heyoka@3.1+mppp", when="@3.1")
        depends_on("heyoka@3.0+mppp", when="@3.0")
        depends_on("heyoka@2.0+mppp", when="@2.0")
        depends_on("heyoka@1.0+mppp", when="@1.0")
        depends_on("heyoka@0.21+mppp", when="@0.21")
    with when("~mppp"):
        depends_on("heyoka@5.1~mppp", when="@5.1")
        depends_on("heyoka@5.0~mppp", when="@5.0")
        depends_on("heyoka@4.0~mppp", when="@4.0")
        depends_on("heyoka@3.2~mppp", when="@3.2")
        depends_on("heyoka@3.1~mppp", when="@3.1")
        depends_on("heyoka@3.0~mppp", when="@3.0")
        depends_on("heyoka@2.0~mppp", when="@2.0")
        depends_on("heyoka@1.0~mppp", when="@1.0")
        depends_on("heyoka@0.21~mppp", when="@0.21")

    # Cloudpickle
    depends_on("py-cloudpickle")
