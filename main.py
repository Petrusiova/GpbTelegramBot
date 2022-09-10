﻿import telebot

bot = telebot.TeleBot('5799725631:AAEYhs-pE1MNRfYlJaMwuju3fZMEKny9WLE')


@bot.message_handler(commands=['start'])
def start(message):
    msg = bot.send_message(message.chat.id,
                           text="Добро пожаловать в <b>паттерны для автоматизации тестирования</b>\n\n"
                                "Шаблоны автоматизации тестирования наиболее полезны, если вы можете сосредоточиться на тех, "
                                "которые действительно помогают решить ваши проблемы. Мы начинаем процесс диагностики:\n\n"

                                "/improve - <b>Улучшение автоматизации тестирования</b> - если Вы недовольны своей текущей автоматизацией или она  не дает вам желаемых преимуществ\n\n"
                                "/no_previous_test_automation - <b>Автоматизации еще не было</b> - если Вы только начинаете с автоматизации и никогда не делали этого раньше\n\n"
                                "/limited_experience - <b>Нет опыта в автоматизации тестирования</b> - если Вы присоединяетесь к команде и не имеете опыта в автоматизации тестирования\n\n"
                                "/test_automation_issues - <b>Конкретные проблемы в автоматизации</b> -если Вы уже знаете какие у вас проблемы с автоматизацией\n\n"

                                "Совет:\n"
                                "- Если первый вариант не соответствует вашей ситуации, вернитесь на эту страницу и попробуйте другой\n\n"
                                "- Если в вашей компании есть разные команды, работающие с автоматизацией, пусть каждая из них сначала выполнит диагностику самостоятельно. \n\n"
                                "/localized_regimes - <b>Локализованные режимы</b> - если проблемы команд существенно отличаются. Это признак того, что каждая команда работает полностью независимо от других, нет обмена экспертизой, методами, стандартами и т. д."
                           , parse_mode='html')


@bot.message_handler(commands=['improve'])
def improve(message):
    msg = bot.send_message(message.chat.id,
                           text="<b>Улучшение автоматизации тестирования</b>\n\n"
                                "Что ниже описывает самую насущную проблему, которую вам нужно решить в данный момент?\n\n"

                                "/lack_of_support - <b>Отсутствие поддержки</b> (со стороны руководства, тестировщиков, разработчиков и т. д.)\n\n"
                                "/lack_of_resources - <b>Нехватка ресурсов</b> (персонал, ПО, оборудование, время и т. д.)\n\n"
                                "/lack_of_direction - <b>Отсутствие направления</b> (что автоматизировать, какую архитектуру реализовать и т. д.)\n\n"
                                "/lack_of_specific_knowledge - <b>Отсутствие конкретных знаний</b> (как протестировать ПО (SUT), какие использовать инструменты, как на самом деле работает автоматизация, написать поддерживаемую автоматизацию и т. д.)\n\n"
                                "/management_expectations_not_met - <b>Ожидания руководства в отношении автоматизации не оправдались</b> (окупаемость инвестиций (ROI), отставание от графика и т. д.)\n\n"
                                "/automation_exec_expectations_not_met - <b>Ожидания от автоматизации не оправдались</b> (скрипты ненадежны или слишком медленны, тесты не могут выполняться самостоятельно и т. д.)\n\n"
                                "/automation_maintenance_expectations_not_met - <b>Ожидания по тех. обслуживанию не оправдались</b> (недокументированные данные или сценарии, отсутствие контроля версий и т. д.)\n\n"

                                "Примечание:\n\n"
                                "Если более одного ответа подходит для вашего случая, начните с самого сложного. После того, как вы решите его, вернитесь к этому вопросу и займитесь следующими.\n\n"
                                "Если вы хотите возродить автоматизацию тестирования, то переходите к проблеме:\n\n"
                                "/stalled_automation - <b>Автоматизация утеряна</b> - чтобы получить обзор возможных шаблонов решения\n\n"

                                "/start - Вернуться к началу процесса диагностики"
                           , parse_mode='html')


@bot.message_handler(commands=['no_previous_test_automation'])
def no_previous_test_automation(message):
    msg = bot.send_message(message.chat.id,
                           text=open('patterns/patterns_no_prev_auto.txt', 'r').read() +

                                "\n\n/set_clear_goals - <b>Установите четкие цели.</b> Эта модель имеет решающее значение. Он должен быть применен в начале любых больших или малых усилий по автоматизации\n\n"
                                "/management_support - <b>Поддержка менеджмента</b> Важно чтобы поддержка автоматизации НЕ выполнялась в одиночку во избежании остановок т.к. информацией владеет только 1 человек\n\n"
                                "/test_automation_owner - <b>Назначенный владелец</b> не только для внедрения автоматизации тестирования, но и для поддержания ее работы в будущем\n\n"
                                "/dedicated_resources - <b>Специальные ресурсы.</b> Эта модель особенно важна в начале новых усилий по автоматизации. В зависимости от размера вашей автоматизации вы можете позже ослабить ее использование.\n\n"
                                "/right_tools - <b>Правильные инструменты.</b> Этот шаблон необходим не только для длительной автоматизации, но и для быстрых исправлений\n\n"
                                "/automation_roles - <b>Роли автоматизации.</b> Используйте этот шаблон для заполнения ролей, необходимых для разработки тестового программного обеспечения автоматизации. Если возможно, используйте /whole_team_approach - <b>Подход всей команды</b> - и по необходимости /get_training - проводите <b>Обучение для команды</b>\n\n"
                                "/plan_support_activities - <b>Планирование деятельности по поддержке.</b> Не забудьте применить этот шаблон, если вы хотите иметь возможность соблюдать свои расписания. Недостающая поддержка со стороны специалистов может довольно эффективно заземлить проект!\n\n"
                                "/maintainable_testware - <b>Поддерживаемое тестовое обеспечение.</b> Применяйте этот шаблон с самого начала, если вы хотите, чтобы ваши усилия по автоматизации были длительными, а расходы на техническое обслуживание были низкими.\n\n"
                                "/automate_whats_needed - <b>Автоматизируйте то что нужно.</b> Этот шаблон показывает вам, как выбрать функции, наиболее достойные автоматизации\n\n"
                                "/take_small_steps - <b>Маленькие шаги</b> Эта модель особенно важна в начале, но ее всегда следует иметь в виду\n\n"
                                "/unattended_test_execution - <b>Необратимое выполнение теста.</b> Этот шаблон дает вам последние предложения о том, как закончить с автоматизацией тестирования\n\n"

                                "/start - Вернуться к началу процесса диагностики"
                           , parse_mode='html')


@bot.message_handler(commands=['limited_experience'])
def limited_experience(message):
    msg = bot.send_message(message.chat.id,
                           text=open('limitedExperience/limitedExperience.txt', 'r').read() +
                                "\n/tester - <b>Тестировщик</b>\n\n"
                                "/developer - <b>Разработчик</b>\n\n"
                                "/test_manager - <b>Тест-менеджер</b>\n\n"

                                "Наиболее рекумендуемые:\n\n"

                                "/check_to_learn - <b>Проверка</b> - позвольте новым членам команды учиться, проверяя работоспособность существующего тестового ПО\n\n"
                                "/document_the_testware - <b>Документация тестового обеспечения</b> - используйте с самого начала автоматизации\n\n"
                                "/do_a_pilot - <b>Подготовка пилота</b> - используйте при запуске автоматизации, чтобы члены команды могли научиться\n\n"
                                "/get_training - <b>Обучение для команды</b> -  после выбора инструментов и архитектуры, а также для тестировщиков, чтобы научиться писать тест-кейсы, подходящие для автоматизации.\n\n"
                                "/ask_for_help - <b>Просьба о помощи</b> - просить о помощи - это не трудно\n\n"

                                "Также полезно:\n\n"

                                "/pair_up - <b>Модель выбора</b> - когда новички должны интегрироваться в команду как можно быстрее\n\n"
                                "/take_small_steps - <b>Маленькие шаги</b> - Москва не сразу строилась\n\n"
                                "/steel_thread - <b>Стальная нить</b> - хороший шаблон для обучения автоматизации тестирования через SUT\n\n"
                                "/prefer_familiar_solutions - <b>Знакомые решения</b> - если члены команды уже используют инструменты или процессы, которые могут быть успешно применены также к проекту автоматизации тестирования.\n\n"

                                "/start - Вернуться к началу процесса диагностики"

                           , parse_mode='html')


@bot.message_handler(commands=['test_automation_issues'])
def test_automation_issues(message):
    msg = bot.send_message(message.chat.id,
                           text=open('testAutoIssues/testAutoIssues.txt', 'r').read() +
                                "\n/inefficient_failure_analysis - <b>Неэффективный анализ сбоев</b>\n\n"
                                "/hard_to_automate - <b>Трудности автоматизации</b>\n\n"
                                "Однако одной из основных причин неудачи является сосредоточение исключительно на технических аспектах. Другие проблемы связаны с тем, как вы работаете, такие как:\n\n"
                                "/late_test_case_design - <b>Поздний тест-дизайн</b>\n\n"
                                "/stalled_automation - <b>Автоматизация утеряна</b> - когда автоматизация, кажется, начинается хорошо, но затем останавливается\n\n"
                                "/high_roi_expectations - <b>Ожидание высокой рентабельности</b>\n\n"

                                "Некоторые проблемы могут возникнуть из-за технических или управленческих проблем."
                                "Мы классифицируем проблемы на следующие категории:\n\n"

                                "/process_issues - <b>Проблемы процесса</b> - как мы работаем с автоматизированными тестами и инструментами\n\n"
                                "/management_issues - <b>Проблемы управления</b> - вопросы управления, кадрового расписания, целей (необходимо время, деньги или люди для исправления)\n\n"
                                "/design_issues - <b>Проблемы проектирования</b> - архитектура тестового программного обеспечения, включая ремонтопригодность\n\n"
                                "/execution_issues - <b>Проблемы с выполнением</b> - запуск тестов в их автоматизированной форме\n\n"

                                "Обратите внимание на:\n\n"

                                "/failure_patterns - <b>Шаблоны отказов</b> - также являются своего рода проблемой, потому что они описывают поведение, которое, если не будет признано вовремя, может поставить под угрозу даже, казалось бы, успешные проекты автоматизации тестирования. Их также называют 'антипаттернами'.\n\n"

                                "/start - Вернуться к началу процесса диагностики"

                           , parse_mode='html')


@bot.message_handler(commands=['localized_regimes'])
def localized_regimes(message):
    msg = bot.send_message(message.chat.id,
                           text="<b>Локализованные режимы</b>\n\n"
                                "Краткое описание проблемы:\n\n"
                                "Использование инструментов или архитектура тестового программного обеспечения отличается от команды к команде\n\n"
                                "Этот вопрос тесно связан с\n\n"

                                "/framework_competition - <b>Структурным соревнованием</b>\n\n"

                                + open('localizedRegimes/localizedRegimes.txt', 'r').read() +

                                "\n/design_for_reuse - <b>Проектируйте для переиспользования</b>\n\n"
                                "/dont_reinvent_the_wheel - <b>Не изобретайте колесо</b> - используйте доступные ноу-хау, инструменты и процессы, когда это возможно.\n\n"
                                "/set_standarts - <b>Стандартизация</b> - установите и следуйте стандартам для артефактов автоматизации\n\n"
                                "/test_automation_owner - <b>Ответственный</b> - назначьте ответственного за автоматизацию тестирования\n\n"

                                "Другие полезные шаблоны::\n\n"

                                "/get_training - <b>Обучение для команды</b> - планируйте обучение для всех, кто участвует в проекте автоматизации тестирования\n\n"
                                "/share_information - <b>Поделиться информацией</b> - запрашивайте и предоставляйте информацию менеджерам, разработчикам, другим тестировщикам и клиентам\n\n"

                                "/start - Вернуться к началу процесса диагностики"

                           , parse_mode='html')


@bot.message_handler(commands=['lack_of_support'])
def lack_of_support(message):
    msg = bot.send_message(message.chat.id,
                           text="<b>Отсутствие поддержки</b>\n\n"
                                "Какой поддержки вам не хватает?\n\n"
                                "Если вам не хватает поддержки определенным образом, одно из следующих идей может дать вам идеи:\n\n"

                                "/managers_dont_see_the_value - <b>Менеджеры не видят ценности</b> - руководство поддерживает только на словах и/или уделяют автоматизации низкий приоритет\n\n"
                                "/testers_dont_help_the_automation_team - <b>Тестировщики не помогают команде автоматизации</b> \n\n"
                                "/developers_dont_help_the_automation_team - <b>Разработчики не помогают команде автоматизации</b>\n\n"
                                "/specialists_dont_help_the_automation_team - <b>Специалисты не помогают команде автоматизации </b> с особыми проблемами автоматизации (базы данных, сети и т. д.)\n\n"
                                "/nobody_helps_new_automators - <b>Никто не помогает новым автоматизаторам</b>\n\n"
                                "/unrealistic_expectations - <b>Нереалистичные ожидания</b> - руководство ожидало 'магию' от инструмента\n\n"
                                "/inadequate_support - <b>Недостаток поддержки</b> - если вы столкнулись с отсутствием поддержки сразу в нескольких областях\n\n"


                                "/improve - Вернуться к началу улучшения автоматизации тестирования\n"
                                "/start - Вернуться к началу процесса диагностики"
                           , parse_mode='html')


@bot.message_handler(commands=['lack_of_resources'])
def lack_of_resources(message):
    msg = bot.send_message(message.chat.id,
                           text="<b>Нехватка ресурсов</b>\n\n"

                                "/ad_hoc_automation - <b>Интуитивная автоматизация</b> - если у вас возникают такие проблемы как:\n\n"

                                "- Расходы на ресурсы автоматизации тестирования не были предусмотрены в бюджете\n\n"
                                "- Недостаточно машин для запуска автоматизации\n\n"
                                "- Базы данных для автоматизации должны использоваться совместно с разработкой или тестированием\n\n"
                                "- Недостаточно лицензий на инструменты\n\n"

                                "Больше причин нехватки ресурсов:\n\n"
                                "/schedule_slip - <b>Скользящее расписание</b> - время на автоматизацию не запланировано или его недостаточно\n\n"
                                "/limited_experience - <b>Нет опыта в автоматизации тестирования</b> - обучение автоматизации не планировалось\n\n"
                                "/inadecuate_team - <b>Недостаточная команда</b> - никому не было поручено заниматься автоматизацией, это делается отдельно в свободное время\n\n"


                                "/improve - Вернуться к началу улучшения автоматизации тестирования\n"
                                "/start - Вернуться к началу процесса диагностики"
                           , parse_mode='html')


@bot.message_handler(commands=['lack_of_direction'])
def lack_of_direction(message):
    msg = bot.send_message(message.chat.id,
                           text="<b>Отсутствие направления</b>\n\n"

                                "/ad_hoc_automation - <b>Интуитивная автоматизация</b> - если у вас возникают такие проблемы как:\n\n"

                                "- никто не отвечает за автоматизацию тестирования, каждый делает то, что считает лучше всего, не сотрудничая с другими.\n\n"
                                "- автоматизация выполняется интуитивно без ведущей стратегии или архитектуры\n\n"

                                "Больше причин отсутствия направления:\n\n"
                                "/inadequate_support - <b>Недостаток поддержки</b> - менеджмент не поддерживает автоматизацию и она выполняется по инициативе 1 человека\n\n"
                                "/manual_mimicry - <b>Ручная мимикрия</b> - автоматизация ручных кейсов происходит как есть\n\n"
                                "/independent_test_cases - <b>Взаимозависимые тесты</b> - автоматизация ручных кейсов происходит как есть(2)\n\n"
                                "/limited_experience - <b>Нет опыта в автоматизации тестирования</b> - тестировщики, занимаясь автоматизацией, не знают как сделать хорошо\n\n"
                                "/localized_regimes - <b>Локализованные режимы</b> - использование инструментов или архитектура тестового ПО отличается от команды к команде\n\n"
                                "/unfocused_automation - <b>Несфокусированная автоматизация</b> - важные тесты не были автоматизированы, только простые\n\n"


                                "/improve - Вернуться к началу улучшения автоматизации тестирования\n"
                                "/start - Вернуться к началу процесса диагностики"
                           , parse_mode='html')


@bot.message_handler(commands=['lack_of_specific_knowledge'])
def lack_of_specific_knowledge(message):
    msg = bot.send_message(message.chat.id,
                           text="<b>Отсутствие конкретных знаний</b>\n\n"

                                "/limited_experience - <b>Нет опыта в автоматизации тестирования</b> - если у вас возникают такие проблемы как:\n\n"

                                "- нет знаний как пользоваться инструментом.\n\n"
                                "- нет знаний что именно автоматизировать\n\n"
                                "- нет знаний как писать автотесты\n\n"

                                "Больше причин отсутствия конкретных знаний:\n\n"
                                "/managers_dont_see_the_value - <b>Менеджеры не видят ценности</b> - менеджмент не знает, что означает автоматизация тестирования\n\n"
                                "/know_how_leakage - <b>Утечка экспертизы</b> - единственный, кто знал об автоматизации, покинул компанию\n\n"
                                "/inadequate_tools - <b>Неадекватные инструменты</b> - нет знаний как выбрать инструмент для автоматизации\n\n"
                                "/inadequate_documentation - <b>Недостаток документации</b> - мало или вообще нет полезной информации о тестируемом ПО в сценариях или другом месте\n\n"
                                "/inadequate_support - <b>Недостаток поддержки</b> - важные тесты не были автоматизированы, только простые\n\n"


                                "/improve - Вернуться к началу улучшения автоматизации тестирования\n"
                                "/start - Вернуться к началу процесса диагностики"
                           , parse_mode='html')


@bot.message_handler(commands=['management_expectations_not_met'])
def management_expectations_not_met(message):
    msg = bot.send_message(message.chat.id,
                           text="<b>Ожидания руководства в отношении автоматизации не оправдались</b>\n\n"

                                "/unrealistic_expectations - <b>Нереалистичные ожидания</b> - руководство ожидало слишком многого от автоматизации\n\n"
                                "/high_roi_expectations - <b>Ожидание высокой рентабельности</b> - ожидаемая окупаемость инвестиций (ROI) не была достигнута\n\n"
                                "/schedule_slip - <b>Скользящее расписание</b> - разработка автоматизации слишком медленная\n\n"
                                "/obscure_management_reports - <b>Неясные отчеты</b> - отчеты по автоматизации слишком сложны для анализа\n\n"
                                "/inefficient_failure_analysis - <b>Неэффективный анализ сбоев</b> - если отчеты о сбоях бесполезны\n\n"

                                "/improve - Вернуться к началу улучшения автоматизации тестирования\n"
                                "/start - Вернуться к началу процесса диагностики"
                           , parse_mode='html')


@bot.message_handler(commands=['automation_exec_expectations_not_met'])
def automation_exec_expectations_not_met(message):
    msg = bot.send_message(message.chat.id,
                           text="<b>Ожидания от автоматизации не оправдались</b>\n\n"

                                "/not_reliable_scripts - <b>Ненадежные скрипты</b> - автоматизированные скрипты не выполняются надежно.\n\n"
                                "/too_slow_scripts - <b>Слишком медленные скрипты</b> - автотесты выполняются слишком медленно\n\n"
                                "/manual_interventions - <b>Ручные вмешательства</b> - автотесты не могут выполняться без присмотра\n\n"
                                "/inadequate_tools - <b>Неадекватные инструменты</b> - текущие инструменты не могут надежно управлять тестируемым ПО\n\n"

                                "/improve - Вернуться к началу улучшения автоматизации тестирования\n"
                                "/start - Вернуться к началу процесса диагностики"
                           , parse_mode='html')


@bot.message_handler(commands=['automation_maintenance_expectations_not_met'])
def automation_maintenance_expectations_not_met(message):
    msg = bot.send_message(message.chat.id,
                           text="<b>Ожидания по тех. обслуживанию не оправдались</b>\n\n"

                                "/maintenance_costs_too_high - <b>Дорогое тех. обслуживание</b> - обслуживание автоматизации (считается) слишком дорогостоящим\n\n"
                                "/not_reusing_existing_data - <b>Данные не переиспользуются</b> - автотесты выполняются слишком медленно\n\n"
                                "/inadequate_documentation - <b>Недостаток документации</b> - нет того, что такое тесты, что делают скрипты, как работает автоматизация\n\n"
                                "/tool_dependency - <b>Зависимость инструмента</b> - автоматизация сделана с помощью инструмента, который больше не подходит\n\n"
                                "/obscure_tests - <b>Неясные тесты</b> - документации нет, поэтому с автоматизацией может работать только ее разработчик\n\n"
                                "/inadequate_revision_control - <b>Неадекватный контроль ревизий</b> - трудно связать автоматизированные скрипты с правильным выпуском тестируемого ПО\n\n"

                                "/improve - Вернуться к началу улучшения автоматизации тестирования\n"
                                "/start - Вернуться к началу процесса диагностики"
                           , parse_mode='html')


@bot.message_handler(commands=['stalled_automation'])
def stalled_automation(message):
    msg = bot.send_message(message.chat.id,
                           text=open('stalledAutomation/stalledAutomation_1.txt', 'r').read() +

                                "/non_technical_testers - <b>Нетехнические тестировщики</b> \n\n" +
                                open('stalledAutomation/stalledAutomation_2.txt', 'r').read() +

                                "Решение:\n\n"
                                "Самые рекомендуемые:\n\n"

                                "/do_a_pilot - <b>Подготовка пилота</b> - узнать, почему усилия по автоматизации зашли в тупик и что с этим делать\n\n"
                                "/lazy_automator - <b>Ленивый автоматизатор</b> - правильный шаблок на автоматизации водиночку\n\n"
                                "/maintain_the_testware - <b>Поддержка тестового обеспечения</b> - вы уже используете этот паттерн. Исключение - брошенная автоматизация\n\n"
                                "/test_automation_owner - <b>Назначенный владелец</b> - назначьте 'владельца'. Если никто не чувствует права собственности на автоматизацию тестирования, никого не будет все равно, успешно это или нет.\n\n"
                                "/whole_team_approach - <b>Подход всей команды</b> - если вы хотите, чтобы ваши усилия по автоматизации тестирования были эффективными и успешными. "
                                "Это будет легко реализовать, если команда разработчиков тестируемого ПО уже приняла гибкий процесс. "
                                "В противном случае вам придется убедить разработчика сделать это, прежде чем вы сможете применить этот шаблон\n\n"

                                "Так же обратите внимание:\n\n"

                                "/abstraction_levels - <b>Уровни абстракции</b> - если тестировщики не могут эффективно использовать инструменты\n\n"
                                "/know_when_to_stop - <b>Знать когда остановиться</b> - этот шаблон поможет вам распознать, что вы не можете автоматизировать все\n\n"
                                "/learn_from_mistakes - <b>Учиться на ошибках</b> - эта модель помогает превратить ошибки в опыт обучения\n\n"
                                "/management_support - <b>Поддержка менеджмента</b> - примените этот шаблон, чтобы получить необходимую поддержку для использования других шаблонов\n\n"
                                "/sell_the_benefits - <b>Продажа преимуществ</b> - шаблон для тестирования solo без необходимой поддержки\n\n"
                                "/take_small_steps - <b>Маленькие шаги</b>  - шаблон, чтобы снова начать работу по автоматизации\n\n"
                                "/test_automation_framework - <b></b> - проверьте, будут ли ваши проблемы решены с помощью этого шаблона\n\n"


                                "/improve - Вернуться к началу улучшения автоматизации тестирования\n"
                                "/start - Вернуться к началу процесса диагностики"
                           , parse_mode='html')


bot.polling(none_stop=True)

# @bot.callback_query_handler(
#     lambda call: call.data == 'diagnostics')
# def layer_0(call):
#     try:
#         if call.data == 'diagnostics':
#             markup = get_diagnostics_markup()
#
#             msg = bot.send_message(call.message.chat.id,
#                                    text="Шаблоны автоматизации тестирования /наиболее /полезны, если вы можете сосредоточиться на тех, "
#                                         "которые действительно помогают решить ваши проблемы. Мы начинаем процесс диагностики, "
#                                         "задавая несколько вопросов. Некоторые приведут вас прямо к конкретной проблеме; "
#                                         "у других будет ряд возможных ответов, которые приведут к более подробным вопросам "
#                                         "или к проблеме, которая лучше всего описывает вашу проблему. "
#                                         "На любом уровне вы сможете вернуться на предыдущий уровень. "
#                                         "Ваши ответы должны помочь определить основные проблемы. "
#                                         "Эти вопросы содержат рекомендации по шаблонам, которые помогут вам решить ваши проблемы. "
#                                         "В /шаблонах разрешения мы даем некоторые рекомендации, но выбор того, "
#                                         "как применять шаблоны, — это то, о чем вам нужно будет подумать в вашей собственной ситуации.",
#
#                                    reply_markup=markup)
#             bot.register_next_step_handler(msg, layer_1)
#         else:
#             pass
#     except:
#         bot.send_message(call.message.chat.id, f'🚫 | Ошибка при выполнении команды')
#
#
# @bot.callback_query_handler(
#     lambda call: call.data == 'improve' or call.data == 'patterns' or call.data == 'experience' or call.data == 'problems' or call.data == 'back')
# def layer_1(call):
#     try:
#
#         if call.data == 'improve':
#             markup = get_improve_markup()
#
#             msg = bot.send_message(call.message.chat.id,
#                                    text='Что ниже описывает наиболее насущную проблему, которую вам предстоит решить на данный момент?\n'
#                                         'Если вы обнаружите, что более одного ответа подходит для вашего случая, начните с самого сложного. После того, как вы решите его, вы должны вернуться к этому вопросу и заняться следующими.',
#                                    reply_markup=markup)
#             bot.register_next_step_handler(msg, layer_1)
#
#         elif call.data == 'patterns':
#             markup = get_patterns_markup()
#
#             msg = bot.send_message(call.message.chat.id,
#                                    text=open('patterns/patterns_no_prev_auto.txt', 'r').read(), parse_mode='Markdown',
#                                    reply_markup=markup)
#             bot.register_next_step_handler(msg, layer_1)
#
#     except:
#         bot.send_message(call.message.chat.id, f'🚫 | Ошибка при выполнении команды')
