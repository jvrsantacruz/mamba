from mamba import describe, context, before, after
from sure import expect


with describe('HooksIsolated') as _:

    _.calls = []

    with context('when executing first context'):

        def it_executes_this_spec_in_first_place():
            expect(_.calls).to.be.empty

    with context('when executing a context with hooks without specs in second place'):

        @before.each
        def add_a_call_in_before_hook():
            _.calls.append('before')

        @after.each
        def add_a_call_in_after_hook():
            _.calls.append('after')

    with context('when executing third context'):

        def it_does_not_execute_any_hook_without_an_spec():
            expect(_.calls).to.be.empty

