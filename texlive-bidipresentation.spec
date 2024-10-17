Name:		texlive-bidipresentation
Version:	35267
Release:	2
Summary:	Experimental bidi presentation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bidipresentation
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bidipresentation.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bidipresentation.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A great portion of the code is borrowed from the texpower
bundle, with modifications to get things working properly in
both right to left and left to right modes.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/xelatex/bidipresentation
%doc %{_texmfdistdir}/doc/xelatex/bidipresentation

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
