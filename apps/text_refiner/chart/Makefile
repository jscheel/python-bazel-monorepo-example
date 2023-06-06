.PHONY: confirm_kubectl get-dir
CHART_GROOVE_TEXT_REFINEMENT_APP_DIR?=`cd ../../python-monorepo/stack/text-refiner; pwd`
CHART_GROOVE_PYTHON_COMMONLIBS_DIR?=`cd ../../python-monorepo/libs; pwd`

confirm_kubectl:
	@../../bin/ensure-local-kubectl-context

update: confirm_kubectl
	test -e ${CHART_GROOVE_TEXT_REFINEMENT_APP_DIR} && \
	test -e ${CHART_GROOVE_PYTHON_COMMONLIBS_DIR} && \
	helm upgrade groove-text-refiner . \
		--install \
		--values values.development.yaml \
		--set hostMountPath=${CHART_GROOVE_TEXT_REFINEMENT_APP_DIR} \
		--set hostCommonLibsMountPath=${CHART_GROOVE_PYTHON_COMMONLIBS_DIR}

get-dir:
	@echo ${CHART_GROOVE_TEXT_REFINEMENT_APP_DIR}

console:
	kubectl exec --stdin --tty `kubectl get pods -l "app.kubernetes.io/instance=groove-text-refiner" --no-headers -o custom-columns=":metadata.name" | head -n 1` -- sh -l

logs:
	kubectl logs -f --tail 100  `kubectl get pods -l "app.kubernetes.io/instance=groove-text-refiner" --no-headers -o custom-columns=":metadata.name" | head -n 1`

rebuild: delete dev

image:
	cd ${CHART_GROOVE_TEXT_REFINEMENT_APP_DIR} && make secrets-dev && make image-dev

image-delete:
	cd ${CHART_GROOVE_TEXT_REFINEMENT_APP_DIR} && make image-dev-delete; echo 'ok'

rebuild-full: image-delete image delete dev

deploy-dev: confirm_kubectl image update

uninstall-dev: confirm_kubectl
	helm delete groove-text-refiner; echo 'ok'

# deploy-staging:
# 	helm upgrade groove-text-refiner . \
# 		--set enviroment=staging \
# 		--install \
# 		--values values.staging.yaml \
# 		--kube-context eks_groove-staging-core \
# 		--set image.tag=`cd ../../text-refiner && git log -1 --pretty=%H`

# deploy-production:
# 	helm upgrade groove-text-refiner . \
# 		--set enviroment=production \
# 		--install \
# 		--values values.production.yaml \
# 		--kube-context eks_groove-production-core \
# 		--set image.tag=`cd ../../text-refiner && git log -1 --pretty=%H`

# uninstall-staging:
# 	helm delete groove-text-refiner --kube-context eks_groove-staging-core

# package-staging:
# 	rm -f *.tgz
# 	$(eval REPO_URL=$(shell helm repo list | grep groove-charts-staging | awk '{print $$2}'))
# 	$(eval CHART_VERSION=$(shell cat Chart.yaml | grep version | awk '{print $$2}'))
# 	cp values.staging.yaml values.yaml
# 	helm package .
# 	rm values.yaml
# 	curl --data-binary "@groove-text-refiner-$(CHART_VERSION).tgz" "$(REPO_URL)/api/charts"; echo
# 	rm "groove-text-refiner-$(CHART_VERSION).tgz"

# package-production:
# 	rm -f *.tgz
# 	$(eval REPO_URL=$(shell helm repo list | grep groove-charts-production | awk '{print $$2}'))
# 	$(eval CHART_VERSION=$(shell cat Chart.yaml | grep version | awk '{print $$2}'))
# 	cp values.production.yaml values.yaml
# 	helm package .
# 	rm values.yaml
# 	curl --data-binary "@groove-text-refiner-$(CHART_VERSION).tgz" "$(REPO_URL)/api/charts"; echo
# 	rm "groove-text-refiner-$(CHART_VERSION).tgz"
