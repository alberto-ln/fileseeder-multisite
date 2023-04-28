import { graphql, PageProps } from "gatsby";
import React from "react";

${IMPORTS}

const ${namePage} = ({ data }: PageProps<Queries.${namePage}Query>) => {
  return (
    <Layout>
      ${LAYOUT}
    </Layout>
  )
}

export default ${namePage};

export const Head = () => <SEO />;

export const query = graphql`
    query ${namePage}{
        site {
            buildTime(formatString: "YYYY-MM-DD hh:mm a z")
        }
    }
`;