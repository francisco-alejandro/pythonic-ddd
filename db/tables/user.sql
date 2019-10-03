CREATE TABLE IF NOT EXISTS public."user"
(
    id uuid NOT NULL,
    email character varying(255) COLLATE pg_catalog."default",
    money_id uuid,
    CONSTRAINT user_pkey PRIMARY KEY (id),
    CONSTRAINT user_money_id_fkey FOREIGN KEY (money_id)
        REFERENCES public.wallet (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)
WITH (
    OIDS = FALSE
)