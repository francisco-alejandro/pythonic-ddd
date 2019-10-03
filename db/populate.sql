INSERT INTO public.wallet(id, currency, value) 
VALUES 
    ('7a8477e5-b8b2-4258-8771-aa21bd1437c5', 'eur', 100),
    ('ac10c82c-e152-474d-b72d-1d40e7b51229', 'eur', 100)
ON CONFLICT DO NOTHING;


INSERT INTO public."user"(id, email, money_id)
VALUES 
    ('826d26eb-a820-4a2f-a453-69731484799b', 'user1@example.com', '7a8477e5-b8b2-4258-8771-aa21bd1437c5'),
    ('9d2c74aa-490b-4c41-9b93-99f5ca55cf71', 'user2@example.com', 'ac10c82c-e152-474d-b72d-1d40e7b51229')
ON CONFLICT DO NOTHING;   