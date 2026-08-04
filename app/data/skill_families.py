"""
=========================================================
JobHunter AI

Skill Knowledge Base

Version : 2.0

This file represents the master knowledge base used by

• Resume Review
• ATS Engine
• Job Finder
• AI Role Inference
• Resume Builder
• Learning Roadmap

Each family represents one capability.

Multiple related keywords contribute to the same skill family.
=========================================================
"""

SKILL_FAMILIES = {

    # =====================================================
    # Artificial Intelligence
    # =====================================================

    "Artificial Intelligence": {

        # Core AI

        "ai",
        "artificial intelligence",
        "machine intelligence",
        "intelligent systems",
        "intelligent automation",

        # Machine Learning

        "machine learning",
        "ml",
        "supervised learning",
        "unsupervised learning",
        "reinforcement learning",
        "deep learning",
        "neural networks",

        # Generative AI

        "generative ai",
        "gen ai",
        "genai",
        "foundation model",
        "foundation models",

        # Large Language Models

        "llm",
        "large language model",
        "large language models",

        "gpt",
        "gpt-3",
        "gpt-3.5",
        "gpt-4",
        "gpt-4o",
        "gpt-5",

        "chatgpt",

        "openai",

        "claude",

        "gemini",

        "copilot",

        "perplexity",

        "llama",
        "llama2",
        "llama3",

        "mistral",

        "phi",

        # Prompt Engineering

        "prompt engineering",
        "prompt design",
        "prompt optimization",

        "few shot prompting",
        "zero shot prompting",

        "chain of thought",

        # Retrieval

        "rag",
        "retrieval augmented generation",

        "vector database",
        "vector search",

        "embedding",
        "embeddings",

        "semantic search",

        # AI Frameworks

        "langchain",

        "langgraph",

        "llamaindex",

        "crewai",

        "autogen",

        "haystack",

        # Agentic AI

        "ai agent",
        "ai agents",

        "agentic ai",

        "autonomous agents",

        "multi agent",

        # MCP

        "mcp",

        "model context protocol",

        # APIs

        "openai api",

        "anthropic api",

        "gemini api",

        "function calling",

        "tool calling",

        # Evaluation

        "hallucination",

        "grounding",

        "guardrails",

        "prompt injection",

        "ai safety",

        "responsible ai"

    },


    # =====================================================
    # Customer Success
    # =====================================================

    "Customer Success": {

        "customer success",
        "customer success manager",
        "customer success lead",
        "customer success specialist",
        "customer onboarding",
        "customer enablement",
        "customer adoption",
        "customer engagement",
        "customer advocacy",
        "customer experience",
        "customer journey",
        "customer lifecycle",
        "customer retention",
        "customer loyalty",
        "customer satisfaction",
        "customer delight",
        "customer health",
        "customer health score",
        "customer success metrics",
        "customer education",
        "customer training",
        "customer implementation",
        "implementation",
        "implementation specialist",
        "implementation manager",
        "success planning",
        "success plan",
        "value realization",
        "value delivery",
        "voice of customer",
        "voc",
        "renewal",
        "renewals",
        "renewal management",
        "expansion",
        "upsell",
        "upselling",
        "cross sell",
        "cross selling",
        "nrr",
        "net revenue retention",
        "grr",
        "gross revenue retention",
        "customer churn",
        "churn reduction",
        "executive business review",
        "ebr",
        "quarterly business review",
        "qbr",
        "business review",
        "health check",
        "stakeholder management",
        "executive stakeholder",
        "stakeholder engagement",
        "relationship building",
        "strategic partnership"

    },

    # =====================================================
    # CRM
    # =====================================================

    "CRM": {

        "crm",
        "customer relationship management",
        "salesforce",
        "salesforce crm",
        "sales cloud",
        "service cloud",
        "hubspot",
        "hubspot crm",
        "zoho",
        "zoho crm",
        "freshsales",
        "freshworks",
        "freshdesk",
        "microsoft dynamics",
        "dynamics 365",
        "oracle crm",
        "sap crm",
        "pipedrive",
        "gainsight",
        "totango",
        "planhat",
        "vitally",
        "zendesk",
        "intercom",
        "highlevel",
        "go high level",
        "customer 360",
        "crm implementation",
        "crm migration",
        "crm customization",
        "crm automation"

    },

    # =====================================================
    # SaaS
    # =====================================================

    "SaaS": {

        "saas",
        "software as a service",
        "subscription",
        "subscription model",
        "subscription business",
        "annual recurring revenue",
        "arr",
        "monthly recurring revenue",
        "mrr",
        "customer lifetime value",
        "cltv",
        "usage analytics",
        "license management",
        "seat management",
        "usage monitoring",
        "product adoption",
        "digital adoption",
        "feature adoption",
        "enterprise software",
        "cloud software",
        "b2b saas",
        "b2c saas",
        "product led growth",
        "plg",
        "customer onboarding",
        "technical onboarding",
        "implementation",
        "professional services",
        "success platform"

    },

    # =====================================================
    # Account Management
    # =====================================================

    "Account Management": {

        "account management",
        "account manager",
        "enterprise account manager",
        "key account manager",
        "key account management",
        "strategic account manager",
        "technical account manager",
        "client partner",
        "client management",
        "client relationship",
        "relationship management",
        "account planning",
        "account growth",
        "account expansion",
        "enterprise accounts",
        "major accounts",
        "global accounts",
        "named accounts",
        "territory management",
        "portfolio management",
        "commercial management",
        "commercial strategy",
        "contract negotiation",
        "contract renewal",
        "client retention",
        "executive relationship",
        "stakeholder alignment"

    },

    # =====================================================
    # Business Development
    # =====================================================

    "Business Development": {

        "business development",
        "business development manager",
        "enterprise sales",
        "solution selling",
        "consultative selling",
        "strategic selling",
        "sales management",
        "sales strategy",
        "sales planning",
        "pipeline management",
        "sales pipeline",
        "lead generation",
        "prospecting",
        "cold calling",
        "cold email",
        "inside sales",
        "outside sales",
        "opportunity management",
        "revenue growth",
        "forecasting",
        "territory planning",
        "territory management",
        "market expansion",
        "go to market",
        "go-to-market",
        "gtm",
        "g2m",
        "partner management",
        "channel sales",
        "partner ecosystem",
        "strategic alliances",
        "sales enablement",
        "rfp",
        "rfi",
        "proposal management",
        "bid management",
        "client acquisition",
        "new business",
        "hunter sales",
        "farmer sales"

    },
    # =====================================================
    # Programming Languages
    # =====================================================

    "Programming Languages": {

        "python",
        "java",
        "javascript",
        "typescript",
        "c",
        "c++",
        "c#",
        ".net",
        "go",
        "golang",
        "rust",
        "php",
        "ruby",
        "swift",
        "kotlin",
        "scala",
        "r",
        "matlab",
        "perl",
        "shell scripting",
        "bash",
        "powershell",
        "objective c",
        "dart",
        "groovy",
        "vb.net"

    },

    # =====================================================
    # Frontend Development
    # =====================================================

    "Frontend Development": {

        "html",
        "html5",
        "css",
        "css3",
        "sass",
        "scss",
        "bootstrap",
        "tailwind css",
        "tailwind",
        "javascript",
        "typescript",
        "jquery",
        "react",
        "react js",
        "reactjs",
        "next.js",
        "nextjs",
        "vue",
        "vue.js",
        "vuejs",
        "angular",
        "angularjs",
        "svelte",
        "redux",
        "webpack",
        "vite",
        "material ui",
        "mui",
        "chakra ui",
        "responsive design",
        "web accessibility",
        "seo"

    },

    # =====================================================
    # Backend Development
    # =====================================================

    "Backend Development": {

        "node.js",
        "nodejs",
        "express",
        "express.js",
        "nestjs",
        "django",
        "flask",
        "fastapi",
        "spring",
        "spring boot",
        "laravel",
        "symfony",
        "ruby on rails",
        "rails",
        ".net core",
        "asp.net",
        "rest api",
        "restful api",
        "graphql",
        "grpc",
        "microservices",
        "api gateway",
        "authentication",
        "authorization",
        "oauth",
        "jwt",
        "websocket",
        "soap",
        "serverless"

    },

    # =====================================================
    # Mobile Development
    # =====================================================

    "Mobile Development": {

        "android",
        "ios",
        "react native",
        "flutter",
        "swift",
        "swiftui",
        "kotlin",
        "java android",
        "xcode",
        "android studio",
        "firebase",
        "push notifications",
        "mobile ui",
        "mobile ux",
        "cross platform",
        "hybrid app",
        "native app",
        "app store",
        "play store"

    },

    # =====================================================
    # Databases
    # =====================================================

    "Databases": {

        "sql",
        "mysql",
        "postgresql",
        "postgres",
        "sqlite",
        "oracle",
        "oracle db",
        "sql server",
        "microsoft sql server",
        "mongodb",
        "redis",
        "cassandra",
        "dynamodb",
        "firebase firestore",
        "cosmos db",
        "neo4j",
        "elasticsearch",
        "opensearch",
        "database design",
        "database optimization",
        "stored procedures",
        "indexing",
        "normalization",
        "nosql"

    },
    # =====================================================
    # Cloud Computing
    # =====================================================

    "Cloud Computing": {

        "aws",
        "amazon web services",
        "ec2",
        "s3",
        "rds",
        "iam",
        "lambda",
        "cloudfront",
        "route53",
        "ecs",
        "eks",
        "fargate",
        "vpc",
        "cloudwatch",
        "azure",
        "microsoft azure",
        "azure functions",
        "azure devops",
        "azure storage",
        "azure app service",
        "azure virtual machines",
        "azure sql",
        "gcp",
        "google cloud",
        "google cloud platform",
        "cloud run",
        "cloud functions",
        "bigquery",
        "cloud storage",
        "cloud computing",
        "multi cloud",
        "hybrid cloud",
        "private cloud",
        "public cloud",
        "cloud migration",
        "cloud architecture"

    },

    # =====================================================
    # DevOps
    # =====================================================

    "DevOps": {

        "devops",
        "docker",
        "docker compose",
        "kubernetes",
        "helm",
        "jenkins",
        "github actions",
        "gitlab ci",
        "bitbucket pipelines",
        "azure devops",
        "ci",
        "cd",
        "ci/cd",
        "continuous integration",
        "continuous deployment",
        "terraform",
        "cloudformation",
        "ansible",
        "chef",
        "puppet",
        "linux",
        "ubuntu",
        "redhat",
        "bash",
        "shell scripting",
        "nginx",
        "apache",
        "reverse proxy",
        "monitoring",
        "grafana",
        "prometheus",
        "elk",
        "elastic stack",
        "logstash",
        "kibana",
        "observability",
        "infrastructure as code",
        "iac"

    },

    # =====================================================
    # Cyber Security
    # =====================================================

    "Cyber Security": {

        "cyber security",
        "information security",
        "network security",
        "application security",
        "endpoint security",
        "penetration testing",
        "ethical hacking",
        "vulnerability assessment",
        "vulnerability management",
        "owasp",
        "oauth",
        "jwt",
        "ssl",
        "tls",
        "encryption",
        "data encryption",
        "identity management",
        "access management",
        "iam",
        "zero trust",
        "security audit",
        "soc",
        "siem",
        "firewall",
        "vpn",
        "incident response",
        "security compliance",
        "iso 27001",
        "gdpr"

    },

    # =====================================================
    # Analytics
    # =====================================================

    "Analytics": {

        "analytics",
        "business analytics",
        "business intelligence",
        "bi",
        "dashboard",
        "reporting",
        "report automation",
        "kpi",
        "metrics",
        "data visualization",
        "excel",
        "advanced excel",
        "pivot table",
        "vlookup",
        "xlookup",
        "power query",
        "power pivot",
        "power bi",
        "tableau",
        "looker",
        "looker studio",
        "google data studio",
        "qlik",
        "sisense",
        "sql",
        "data analysis",
        "trend analysis",
        "forecasting",
        "predictive analytics"

    },

    # =====================================================
    # Data Engineering
    # =====================================================

    "Data Engineering": {

        "data engineering",
        "etl",
        "elt",
        "data pipeline",
        "data warehouse",
        "data lake",
        "data mart",
        "apache spark",
        "spark",
        "hadoop",
        "airflow",
        "databricks",
        "snowflake",
        "redshift",
        "bigquery",
        "kafka",
        "stream processing",
        "batch processing",
        "data modeling",
        "data governance",
        "data quality",
        "data integration",
        "master data management",
        "mdm"

    },
    # =====================================================
    # UI / UX Design
    # =====================================================

    "UI/UX": {

        "ui",
        "ux",
        "ui design",
        "ux design",
        "user interface",
        "user experience",
        "interaction design",
        "wireframing",
        "prototyping",
        "figma",
        "adobe xd",
        "sketch",
        "invision",
        "design system",
        "responsive design",
        "mobile first design",
        "accessibility",
        "wcag",
        "usability testing",
        "user research",
        "information architecture",
        "visual design",
        "design thinking"

    },

    # =====================================================
    # Quality Assurance
    # =====================================================

    "Quality Assurance": {

        "qa",
        "quality assurance",
        "software testing",
        "manual testing",
        "automation testing",
        "selenium",
        "cypress",
        "playwright",
        "test automation",
        "regression testing",
        "functional testing",
        "integration testing",
        "system testing",
        "uat",
        "user acceptance testing",
        "performance testing",
        "load testing",
        "api testing",
        "postman",
        "jmeter",
        "bug tracking",
        "jira"

    },

    # =====================================================
    # Project Management
    # =====================================================

    "Project Management": {

        "project management",
        "project planning",
        "project delivery",
        "program management",
        "portfolio management",
        "agile",
        "scrum",
        "kanban",
        "safe",
        "waterfall",
        "jira",
        "confluence",
        "risk management",
        "resource planning",
        "roadmap",
        "milestone planning",
        "change management",
        "stakeholder communication",
        "budget management",
        "scope management"

    },

    # =====================================================
    # Leadership
    # =====================================================

    "Leadership": {

        "leadership",
        "people management",
        "team management",
        "team leadership",
        "coaching",
        "mentoring",
        "performance management",
        "strategic planning",
        "decision making",
        "problem solving",
        "conflict resolution",
        "cross functional collaboration",
        "organizational leadership",
        "executive leadership",
        "vision",
        "goal setting",
        "delegation"

    },

    # =====================================================
    # Soft Skills
    # =====================================================

    "Soft Skills": {

        "communication",
        "presentation",
        "public speaking",
        "negotiation",
        "relationship management",
        "stakeholder management",
        "active listening",
        "critical thinking",
        "analytical thinking",
        "time management",
        "adaptability",
        "collaboration",
        "teamwork",
        "creativity",
        "innovation",
        "emotional intelligence",
        "customer focus",
        "ownership",
        "attention to detail"

    },

    # =====================================================
    # Marketing
    # =====================================================

    "Marketing": {

        "digital marketing",
        "content marketing",
        "seo",
        "sem",
        "email marketing",
        "social media marketing",
        "google analytics",
        "google ads",
        "facebook ads",
        "linkedin marketing",
        "campaign management",
        "brand management",
        "marketing automation",
        "hubspot marketing",
        "market research",
        "lead nurturing"

    },

    # =====================================================
    # Human Resources
    # =====================================================

    "Human Resources": {

        "human resources",
        "hr",
        "talent acquisition",
        "recruitment",
        "technical recruitment",
        "interviewing",
        "employee engagement",
        "employee relations",
        "performance appraisal",
        "learning and development",
        "compensation",
        "benefits",
        "succession planning",
        "hr operations",
        "hr analytics"

    },

    # =====================================================
    # Finance
    # =====================================================

    "Finance": {

        "finance",
        "financial analysis",
        "financial planning",
        "budgeting",
        "forecasting",
        "accounting",
        "bookkeeping",
        "cost analysis",
        "profit and loss",
        "balance sheet",
        "cash flow",
        "financial reporting",
        "taxation",
        "audit",
        "sap fico",
        "oracle financials"

    },

    # =====================================================
    # Operations
    # =====================================================

    "Operations": {

        "operations",
        "business operations",
        "process improvement",
        "process optimization",
        "standard operating procedures",
        "sop",
        "workflow automation",
        "continuous improvement",
        "lean",
        "six sigma",
        "vendor management",
        "procurement",
        "supply chain",
        "inventory management",
        "service delivery",
        "operational excellence"

    }

}