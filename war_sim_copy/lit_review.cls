% Intro Options
\ProvidesClass{lit-review}[2019/27/08 CV class]
\NeedsTeXFormat{LaTeX2e}
\DeclareOption{print}{\def\@cv@print{}}
\DeclareOption*{%
  \PassOptionsToClass{\CurrentOption}{article}
}
\ProcessOptions\relax
\LoadClass{article}

% Package Imports
%\usepackage[hmargin=1.25cm, vmargin=0.7cm]{geometry}
\usepackage[hmargin=0.5in, vmargin=0.5in, bottom=0cm]{geometry}
\usepackage[usenames,dvipsnames]{xcolor}
\usepackage[hidelinks]{hyperref}
\usepackage{titlesec}
\usepackage[absolute]{textpos}
\usepackage[UKenglish]{babel}
\usepackage[UKenglish]{isodate}
\usepackage{fontspec,xltxtra,xunicode}

% Color definitions
\definecolor{date}{HTML}{666666} 
\definecolor{primary}{HTML}{2b2b2b} 
\definecolor{headings}{HTML}{0CA4A5}
\definecolor{subheadings}{HTML}{333333}
\definecolor{leftColBackground}{HTML}{D3D3D3} 

% Set main fonts
\defaultfontfeatures{Mapping=tex-text}
\setmainfont[Color=primary]{mathptmx}
\setsansfont[Scale=MatchLowercase,Mapping=tex-text]{mathptmx}
\newcommand{\custombold}[1]{\color{subheadings}\fontspec{mathptmx}\selectfont #1 \normalfont}

% Date command
\setlength{\TPHorizModule}{1mm}
\setlength{\TPVertModule}{1mm}
\textblockorigin{0mm}{5mm} 
\newcommand{\lastupdated}{\begin{textblock}{60}(165,0)
\color{date}\fontspec{mathptmx}\fontsize{8pt}{10pt}\selectfont 
Last Updated on
\today
\end{textblock}}

% Name command
\newcommand{\namesection}[3]{
	\centering{
		\sffamily
		\fontspec{mathptmx}\fontsize{40pt}{10cm}\selectfont #1 
		\fontspec{mathptmx}\selectfont #2
	} \\
	\vspace{5pt}
	\centering{ \color{subheadings}\fontspec{mathptmx}\fontsize{17pt}{19pt}\selectfont #3}
	\noindent\makebox[\linewidth]{\rule{\paperwidth}{0.4pt}}
	\vspace{-41.6pt}
}
\titlespacing{\section}{0pt}{0pt}{0pt}

% Headings command
\titleformat{\section}{\color{headings}
\scshape\fontspec{mathptmx}\fontsize{12pt}{20pt}\selectfont\centering\uppercase}{} {0em}{}

% Subeadings command
\titleformat{\subsection}{\color{subheadings}
\raggedright\fontspec{mathptmx}\fontsize{10pt}{11pt}\selectfont\bfseries}{}{0em}{}
\titlespacing{\subsection}{0pt}{\parskip}{-\parskip}
\titlespacing{\subsubsection}{0pt}{\parskip}{-\parskip}
\newcommand{\runsubsection}[1]{\color{subheadings}
\fontspec{mathptmx}\fontsize{10pt}{11pt}\selectfont\bfseries {#1} \normalfont}

\newcommand{\awards}[1]{\color{subheadings}
\fontspec{mathptmx\fontsize{10pt}{11pt}\selectfont\bfseries {#1} \normalfont}

% Descriptors command
\newcommand{\descript}[1]{\color{subheadings}\raggedright\scshape\fontspec{mathptmx}\fontsize{10pt}{11pt}\selectfont {#1 \\} \normalfont}
\newcommand{\descriptbf}[1]{\color{subheadings}\raggedright\scshape\fontspec{mathptmx}\fontsize{10pt}{11pt}\selectfont {#1 \\} \normalfont}

\newcommand{\descriptit}[1]{\color{subheadings}\raggedright\scshape\fontspec{mathptmx}\fontsize{10pt}{11pt}\selectfont {#1} \normalfont}
% \newcommand{\subdescript}[1]{\color{subheadings}\raggedright\scshape\fontspec[Path = fonts/lato/]{mathptmxRegIta}\fontsize{10pt}{11pt}\selectfont {#1} \normalfont}

% Location command
\newcommand{\location}[1]{\hfill\color{primary}\fontspec[Path = fonts/lato/]{mathptmxLig}\fontsize{10pt}{12pt}\selectfont {#1\\} \normalfont}

% Section seperators command
\newcommand{\sectionsep}[0]{\vspace{8pt}}

% Bullet Lists with fewer gaps command
\newenvironment{tightemize}{\vspace{-\topsep}\begin{itemize}\itemsep1pt \parskip0pt \parsep0pt}{\end{itemize}\vspace{-\topsep}}

% Link icon 
\newcommand{\ExternalLink}{%
    \tikz[x=1.2ex, y=1.2ex, baseline=-0.05ex]{% 
        \begin{scope}[x=1ex, y=1ex]
            \clip (-0.1,-0.1) 
                --++ (-0, 1.2) 
                --++ (0.6, 0) 
                --++ (0, -0.6) 
                --++ (0.6, 0) 
                --++ (0, -1);
            \path[draw, 
                line width = 0.5, 
                rounded corners=0.5] 
                (0,0) rectangle (1,1);
        \end{scope}
        \path[draw, line width = 0.5] (0.5, 0.5) 
            -- (1, 1);
        \path[draw, line width = 0.5] (0.6, 1) 
            -- (1, 1) -- (1, 0.6);
        }
    }