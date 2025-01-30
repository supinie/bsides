with import <nixpkgs> {};
mkShell {
    buildInputs = [ texliveFull texlivePackages.beamer python3 python313Packages.matplotlib python313Packages.numpy ];
}
