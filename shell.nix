with import <nixpkgs> {};
mkShell {
    buildInputs = [ texliveFull texlivePackages.beamer python3 python312Packages.matplotlib python312Packages.numpy ];
}
