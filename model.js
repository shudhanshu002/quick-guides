create table users(
    id bigserial primary key,
    name varchar(100),
    email text unique not null,
    password_hash text not null,
    created_at timestamp not null default now()
);

create table interviews(
    id bigserial primary key,
    title varchar(200) not null,
    language varchar(50) not null,
    difficulty varchar(20) not null,
    status varchar(20) not null,
    user_id BigInt not null,
    created_at timestamp not null default now(),
    constraint fk_interview_user
    foreign key(user_id)
    references users(id)
    on delete cascade 
);

create table questions(
    id bigserial primary key,
    question_text text not null,
    question_order int not null,
    interview_id bigint not null,
    constraint fk_questions_interview foreign key(interview_id) references interviews(id) on delete cascade
);

create table answers(
    id bigserial primary key,
    answer_text test,
    duration int not null,
    question_id bigint unique not null,
    created_at timestamp default now(),
    constraint fk_answer_question foreign key(question_id) references questions(id) on delete cascade
);

CREATE TABLE feedback(
    id BIGSERIAL PRIMARY KEY,
    overall_score INT NOT NULL,
    strengths TEXT,
    weaknesses TEXT,
    suggestions TEXT,
    interview_id BIGINT UNIQUE NOT NULL,
    CONSTRAINT fk_feedback_interview
    FOREIGN KEY(interview_id)
    REFERENCES interviews(id)
    ON DELETE CASCADE,
    CHECK (
        overall_score BETWEEN 0 AND 100
    )
);