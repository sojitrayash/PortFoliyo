import GithubIcon from "./../public/assets/icons/github.svg";
import LinkedInIcon from "./../public/assets/icons/linkedin.svg";
import XIcon from "./../public/assets/icons/x.svg";
import InstagramIcon from "./../public/assets/icons/instagram.svg";
import FrontendIcon from "./../public/assets/icons/frontend.svg";
import LeaderShipIcon from "./../public/assets/icons/leadership.svg";
import ProblemSolvingIcon from "./../public/assets/icons/problem-solving.svg";
import BlockChainIcon from "./../public/assets/icons/blockchain.svg";
import AIIcon from "./../public/assets/icons/ai.svg";
import FreelancerIcon from "./../public/assets/icons/freelance.svg";
import BackendIcon from "./../public/assets/icons/backend.svg";
import FullStackIcon from "./../public/assets/icons/full-stack.svg";

const navLinks = [
  {
    id: "about",
    title: "About",
  },
  {
    id: "work",
    title: "Work",
  },
  {
    id: "skills",
    title: "Skills",
  },
  {
    id: "projects",
    title: "Projects",
  },
  {
    id: "contact",
    title: "Contact",
  },
];

const services = [
  {
    title: "Full Stack Developer",
    icon: <FullStackIcon />,
  },
  {
    title: "Frontend Developer",
    icon: <FrontendIcon />,
  },
  {
    title: "Backend Developer",
    icon: <BackendIcon />,
  },
  {
    title: "Problem Solving",
    icon: <ProblemSolvingIcon />,
  },
  {
    title: "BlockChain Development",
    icon: <BlockChainIcon />,
  },
  {
    title: "Artificial Intelligence Development",
    icon: <AIIcon />,
  },
  {
    title: "Freelancer",
    icon: <FreelancerIcon />,
  },
  {
    title: "Leadership",
    icon: <LeaderShipIcon />,
  },
];

const technologies = {
  languages: [
    {
      name: "HTML5",
      icon: "/assets/tech/html5.svg",
      link: "https://html.spec.whatwg.org/multipage/",
    },
    {
      name: "CSS3",
      icon: "/assets/tech/css3.svg",
      link: "https://www.w3.org/Style/CSS/Overview.en.html",
    },
    {
      name: "JavaScript",
      icon: "/assets/tech/javascript.svg",
      link: "https://262.ecma-international.org/",
    },
    {
      name: "TypeScript",
      icon: "/assets/tech/typescript.svg",
      link: "https://www.typescriptlang.org/",
    },
    {
      name: "C",
      icon: "/assets/tech/c.svg",
      link: "https://en.cppreference.com/w/c",
    },
    {
      name: "Java",
      icon: "/assets/tech/java.svg",
      link: "https://www.java.com/en/",
    },
    {
      name: "Python",
      icon: "/assets/tech/python.svg",
      link: "https://www.python.org/",
    },
    {
      name: "PHP",
      icon: "/assets/tech/php.png",
      link: "https://www.php.net/",
    },
  ],
  frameworks: [
    {
      name: "Next.js",
      icon: "/assets/tech/nextjs.svg",
      link: "https://nextjs.org/",
    },
    {
      name: "TailwindCSS",
      icon: "/assets/tech/tailwindcss.svg",
      link: "https://tailwindcss.com/",
    },
    {
      name: "Express.js",
      icon: "/assets/tech/expressjs.png",
      link: "https://expressjs.com/",
    },
    {
      name: "Flutter",
      icon: "/assets/tech/flutter.svg",
      link: "https://flutter.dev/",
    },
  ],
  libraries: [
    {
      name: "React",
      icon: "/assets/tech/react.svg",
      link: "https://react.dev/",
    },
    {
      name: "Three.js",
      icon: "/assets/tech/threejs.svg",
      link: "https://threejs.org/",
    },
    {
      name: "Styled-Components",
      icon: "/assets/tech/styled-components.png",
      link: "https://styled-components.com/",
    },
    {
      name: "Framer-motion",
      icon: "/assets/tech/framer.svg",
      link: "https://www.framer.com/motion/",
    },
    {
      name: "NextAuth.js",
      icon: "/assets/tech/nextauthjs.png",
      link: "https://next-auth.js.org/",
    },
    {
      name: "Prisma",
      icon: "/assets/tech/prisma.svg",
      link: "https://www.prisma.io/",
    },
  ],
  tools: [
    {
      name: "Git",
      icon: "/assets/tech/git.svg",
      link: "https://git-scm.com/",
    },
    {
      name: "Github",
      icon: "/assets/icons/github.svg",
      link: "https://github.com/",
    },
    {
      name: "Postman",
      icon: "/assets/tech/postman.svg",
      link: "https://www.postman.com/",
    },
    {
      name: "Figma",
      icon: "/assets/tech/figma.svg",
      link: "https://www.figma.com/",
    },
    {
      name: "Docker",
      icon: "/assets/tech/docker.svg",
      link: "https://www.docker.com/",
    },
  ],
  environments: [
    {
      name: "Node.js",
      icon: "/assets/tech/nodejs.svg",
      link: "https://nodejs.org/en",
    },
  ],
  databases: [
    {
      name: "MongoDB",
      icon: "/assets/tech/mongodb.svg",
      link: "https://www.mongodb.com/",
    },
    {
      name: "Firebase",
      icon: "/assets/tech/firebase.svg",
      link: "https://firebase.google.com/",
    },
    {
      name: "MySQL",
      icon: "/assets/tech/my-sql.png",
      link: "https://www.mysql.com/",
    },
  ],
};

const experiences = [
  {
    title: "Software Tester Live Streaming Intern",
    company_name: "Epitome Corporation Pvt Ltd",
    icon: "/assets/company/epitome.png",
    iconBg: "#E6DEDD",
    date: "September 2024 - October 2024",
    points: [
      "My responsibilities included identifying bugs, testing application performance, and verifying functionality under various conditions.",
      "I collaborated with the development team to resolve issues and improve the quality of the live streaming platform.",
      "This role enhanced my attention to detail, troubleshooting abilities, and understanding of software testing processes.",
      "The experience provided valuable insights into real-time systems and the critical role of testing in software development.",
    ],
  },
  {
    title: "Software Devloper",
    company_name: "S & T Traning Institute - Sabarmti",
    icon: "/assets/company/rrb.png",
    iconBg: "#E6DEDD",
    date: "April 2024 - June 2024", 
    points: [
      "I implemented a certificate authentication system to enhance security and streamline the user verification process.",
      "This system utilized digital certificates for verifying identities, ensuring secure access to sensitive applications and resources.",
      "My responsibilities included designing, coding, and testing the authentication framework for seamless integration into existing systems.",
      "The project improved my knowledge of cryptographic protocols, public key infrastructure (PKI), and secure communication techniques.",
      "This experience strengthened my skills in implementing secure, scalable solutions and highlighted the importance of robust authentication mechanisms.",
    ],
  },
  {
    title: "Full Stack Developer Intern",
    company_name: "PavitraSoft Company (Remote)",
    icon: "/assets/company/pavitra.png",
    iconBg: "#E6DEDD",
    date: "April 2023 - February 2024",
    points: [
      "My role involved designing, developing, and maintaining web applications using modern frontend and backend technologies.",
      "I contributed to multiple projects, enhancing my skills in programming, problem-solving, and team collaboration.",
      "This experience improved my technical expertise and prepared me for future challenges in software development.",
      "Working in a professional environment helped me understand industry standards, deadlines, and the importance of client satisfaction.",
    ],
  },
  {
    title: "B.TECH Information Technology",
    company_name: "Aditya Silver Oak Institute of Technology",
    icon: "/assets/company/asoit.png",
    iconBg: "#E6DEDD",
    date: "September 2022 - June 2026",
    points: [
      "I am pursuing a B.Tech in Information Technology to build expertise in programming and problem-solving techniques.",
      "This degree focuses on emerging fields like AI, machine learning, and cybersecurity, shaping future-ready professionals.",
      "Practical exposure through projects and internships enhances my technical skills and prepares me for industry challenges.",
      "The program equips me with the knowledge to contribute to innovations and excel in the dynamic IT industry.",
    ],
  },
];

const testimonials = [
  {
    testimonial:
      "I thought it was impossible to make a website as beautiful as our product, but Rick proved me wrong.",
    name: "Sara Lee",
    designation: "CFO",
    company: "Acme Co",
    image: "https://randomuser.me/api/portraits/women/4.jpg",
  },
  {
    testimonial:
      "I've never met a web developer who truly cares about their clients' success like Rick does.",
    name: "Chris Brown",
    designation: "COO",
    company: "DEF Corp",
    image: "https://randomuser.me/api/portraits/men/5.jpg",
  },
  {
    testimonial:
      "After Rick optimized our website, our traffic increased by 50%. We can't thank them enough!",
    name: "Lisa Wang",
    designation: "CTO",
    company: "456 Enterprises",
    image: "https://randomuser.me/api/portraits/women/6.jpg",
  },
];

const projects = [
  {
    name: "Jarvis AI",
    description:
      "I developed a personal AI assistant named Jarvis using Python, designed to automate tasks, manage schedules, and provide information. Jarvis integrates natural language processing and voice recognition for seamless interaction, making daily activities more efficient and organized.",
    tags: [
      {
        name: "Python",
        color: "blue-text-gradient",
      },
      {
        name: "Library ",
        color: "green-text-gradient",
      },
      {
        name: "API",
        color: "pink-text-gradient",
      },
      
    ],
    image: "/assets/projects/jarvis.png",
    source_code_link: "#",
    deployed_link: "#",
  },
  {
    name: "Matrimony Website",
    description:
      "I developed a matrimony project to connect individuals seeking life partners. The platform included user registration, profile creation, and advanced search features. It also enabled secure communication, ensuring privacy, and streamlined matchmaking through intelligent algorithms.",
    tags: [
      {
        name: "Pyhton",
        color: "blue-text-gradient",
      },
      {
        name: "DJango",
        color: "green-text-gradient",
      },
      {
        name: "Bootstrap",
        color: "pink-text-gradient",
      },
      {
        name: "Jquery",
        color: "orange-text-gradient",
      },
      {
        name: "dbSqlite3",
        color: "yellow-text-gradient",
      },
    ],
    image: "/assets/projects/matrimony.png",
    source_code_link: "#",
    deployed_link: "#",
  },
  
];

const socials = [
  {
    id: "github",
    icon: <GithubIcon />,
    link: "https://github.com/sojitrayash",
  },
  {
    id: "linkedin",
    icon: <LinkedInIcon />,
    link: "https://www.linkedin.com/in/sojitra-yashkumar",
  },
  {
    id: "x",
    icon: <XIcon />,
    link: "https://twitter.com/",
  },
  {
    id: "instagram",
    icon: <InstagramIcon />,
    link: "https://www.instagram.com/",
  },
];

const heroTexts = [
  "React/Next.js developer",
  500,
  "Freelancer",
  500,
  "Full-Stack developer",
  500,
  "Frontend developer",
  500,
  "Backend developer",
  500,
  "BlockChain developer",
  500,
  "Cyber Security",
  500,
  "AI - ML developer",
  500,
];

export {
  navLinks,
  services,
  technologies,
  experiences,
  testimonials,
  projects,
  socials,
  heroTexts,
};
