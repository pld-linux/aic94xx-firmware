Summary:	Firmware for the Adaptec AIC-94xx HBA
Name:		aic94xx-firmware
Version:	1.0.0
Release:	0.V17_10C6
License:	GPL
Group:		Base/Kernel
Source0:	http://kernel.org/pub/linux/kernel/people/jejb/aic94xx-seq.fw
# Source0-md5:	589f442b43ea0cc42fec275d7a612c2e
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the firmware for the aic94xx driver.

%prep
%setup -q -c -T

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware

install %{SOURCE0} $RPM_BUILD_ROOT/lib/firmware

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/lib/firmware/*
