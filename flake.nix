{
  description = "Python dev environment";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixpkgs-unstable";
  };

  outputs = { nixpkgs, ... }: let
    system = "x86_64-linux";
    pkgs = nixpkgs.legacyPackages.${system};
  in {
    devShells.${system}.default = pkgs.mkShellNoCC {
      packages = with pkgs; [
        (python3.withPackages (pyPkgs: with pyPkgs; [
          fastapi
          fastapi-cli
          pydantic
        ]))
        fastapi-cli
      ];
    };
  };
}
