import * as React from "react";
import { PropsWithChildren } from "react";
import { useTranslation } from "react-i18next";

type Props${NAME} = PropsWithChildren<{
    element: string;
}>

const ${NAME}: React.FC<Props${NAME}> = (props: Props${NAME}) => {
  const { t } = useTranslation("global")
  return (
    <div className={`m-${className}`}>
      <h2>Hola! soy ${NAME}, una molécula</h2>
      <p>
        Puedes encontrarme en <code>${DIR_PATH}</code> como {" "}
        <pre>${FILE_NAME}</pre>
      </p>
      <blockquote>{t("global.name")}</blockquote>
      <p>y mi flow parte de esta clase m-${className}, en el mismo dir :) </p>
    </div>
  );
};

export default ${NAME};
