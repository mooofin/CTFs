{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = with pkgs; [
    python311
    python311Packages.pip
    python311Packages.pycryptodome
    python311Packages.yara-python
    python311Packages.capstone
    python311Packages.distorm3
    python311Packages.pefile
    
    sleuthkit
    binwalk
    foremost
    hexedit
    file
    p7zip
    unzip
    git
  ];

  shellHook = ''
    echo "Setting up Volatility 3 environment..."
    
   
    if [ ! -d .venv ]; then
      python -m venv .venv
      source .venv/bin/activate
      pip install --upgrade pip
      pip install volatility3
    else
      source .venv/bin/activate
    fi
    
    echo "Volatility 3 Environment Ready"
    echo "Usage: vol -f <memory.dmp> <plugin>"
    alias vol='python -m volatility3'
    alias vol3='python -m volatility3'
  '';
}
(.venv) 
