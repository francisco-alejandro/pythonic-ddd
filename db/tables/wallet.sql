CREATE TABLE IF NOT EXISTS public.wallet
(
    id uuid NOT NULL,
    currency character varying(3) COLLATE pg_catalog."default",
    value numeric,
    CONSTRAINT wallet_pkey PRIMARY KEY (id)
)
WITH (
    OIDS = FALSE
)