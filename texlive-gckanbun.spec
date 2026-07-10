%global tl_name gckanbun
%global tl_revision 79444

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.6.0
Release:	%{tl_revision}.1
Summary:	Kanbun typesetting for (u)pLaTeX and LuaLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/japanese/gckanbun
License:	mit
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gckanbun.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gckanbun.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a Kanbun (Han Wen , "Chinese writing") typesetting
for (u)pLaTeX and LuaLaTeX.

