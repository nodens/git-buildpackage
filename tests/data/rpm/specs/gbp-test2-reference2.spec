Name:       gbp-test2
Summary:    Test package 2 for git-buildpackage
Epoch:      2
Version:    3.0
Release:    0
Group:      Development/Libraries
License:    GPLv2
Source10:   ftp://ftp.host.com/%{name}-%{version}.tar.gz
Source:     foo.txt
Source20:   bar.tar.gz
# Gbp-Ignore-Patches: -1
Patch:      my.patch
# Patches auto-generated by git-buildpackage:
Patch0:     1.patch
Patch1:     2.patch
Packager:   Markus Lehtonen <markus.lehtonen@linux.intel.com>
VCS:        myvcstag

%description
Package for testing the RPM functionality of git-buildpackage.

%package empty
Summary:    Empty subpackage

%description empty
Empty subpackage for the %{name} test package.


%prep
%setup -T -n %{name}-%{version} -c -a 10

%patch

echo "Do things"

# Gbp-Patch-Macros
# 1.patch
%if true
%patch0 -p1
%endif
# 2.patch
%ifarch %ix86
%patch1 -p1
%endif

%build
make


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_datadir}/%{name}
cp -R * %{buildroot}/%{_datadir}/%{name}
install %{SOURCE0} %{buildroot}/%{_datadir}/%{name}


%changelog
* Tue Feb 04 2014 Name <email> 1
- My change


%files
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}
%{_datadir}/%{name}

%files empty
%defattr(-,root,root,-)
