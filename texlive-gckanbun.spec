Name:		texlive-gckanbun
Version:	61719
Release:	1
Summary:	Kanbun typesetting for (u)pLaTeX and LuaLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gckanbun
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gckanbun.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gckanbun.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a Kanbun (Han Wen , "Chinese writing")
typesetting for (u)pLaTeX and LuaLaTeX.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/gckanbun
%doc %{_texmfdistdir}/doc/latex/gckanbun

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
