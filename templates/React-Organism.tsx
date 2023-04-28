import * as React from "react";
import { PropsWithChildren } from "react";
import { useTranslation } from "react-i18next";

type Props${NAME} = PropsWithChildren<{
    data ?: string | null | undefined;
}>

const ${NAME}: React.FC<Props${NAME}> = (props: Props${NAME}) => {
const { t } = useTranslation("global")
  return (
    <section className={`o-${className}`}>
      <div className={`c-${className}`}>
          <h1>Hola! soy ${NAME},</h1>
          <p>
            Puedes encontrarme en ${DIR_PATH} como ${FILE_NAME}
          </p>
          <blockquote>{t("global.name")}</blockquote>
          <p>
            y mi flow parte de esta clase o-${className}, en el mismo dir :)
          </p>
      </div>
    </section>
  );
};

export {${NAME}};
