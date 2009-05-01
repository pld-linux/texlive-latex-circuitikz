%define short_name circuitikz
%define	texhash	[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;

Summary:	CircuiTikz is a set of LaTeX macros designed to make it easy to draw electrical networks in scientific publications
Summary(hu.UTF-8):	A CircuiTikz LaTeX makrók gyűjteménye, amelyek elektromos hálózatok könnyű rajzolására készült.
Summary(pl.UTF-8):	Zestaw makr LaTeXa do rysowania schematów sieci elektrycznych
Name:		texlive-latex-%{short_name}
Version:	0.2
Release:	1
License:	LaTeX Project Public License
Group:		Applications/Publishing/TeX
URL:		http://home.dei.polimi.it/mredaelli/circuitikz/index.html
Source0:	http://home.dei.polimi.it/mredaelli/downloads/circuitikz.zip
# Source0-md5:	45f4bf3eb88812f1dfacaed0c92f9d8b
Requires(post,postun):	/usr/bin/texhash
Requires:	texlive-latex
Requires:	texlive-latex-pgf
Requires:	unzip
Obsoletes:	tetex-latex-%{short_name}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CircuiTikz is a set of LaTeX macros designed to make it easy to draw
electrical networks in scientific publications.

%description -l hu.UTF-8
A CircuiTikz Latex makrók gyűjteménye, amelyek elektromos hálózatok
könnyű rajzolására készült.

%description -l pl.UTF-8
CircuiTikz jest zbiorem makr LaTeXa mającym ułatwić rysowanie shematów
sieci elektrycznych w publikacjach naukowych.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/texmf-dist/tex/latex/%{short_name}
install tex/latex/%{short_name}/* $RPM_BUILD_ROOT%{_datadir}/texmf-dist/tex/latex/%{short_name}

install -d $RPM_BUILD_ROOT%{_datadir}/texmf-dist/doc/latex/%{short_name}
install doc/latex/%{short_name}/* $RPM_BUILD_ROOT%{_datadir}/texmf-dist/doc/latex/%{short_name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%doc %{_datadir}/texmf-dist/doc/latex/%{short_name}
%{_datadir}/texmf-dist/tex/latex/%{short_name}
