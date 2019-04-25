from conans import ConanFile, CMake, tools


class ReaderwriterqueueConan(ConanFile):
    name = "readerwriterqueue"
    version = "1.0.1"
    url = "https://github.com/Lawrencemm/readerwriterqueue"
    exports_sources = "readerwriterqueue.h", "LICENSE.md", "atomicops.h"
    no_copy_source = True

    def package(self):
        self.copy("readerwriterqueue.h", dst="include")
        self.copy("atomicops.h", dst="include")
        self.copy("LICENSE.md")

